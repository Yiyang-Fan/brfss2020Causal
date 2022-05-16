### This file do an EDA trying to discover the structure by applying
##  PC algorithm to the narrowed data set obtained from DataPreprocessing.py
##  Randomly shuffled the original data and divided it into 10 pieces, each contains 40000 data.
##  Applying PC algorithm to each piece of the data, and compare the obtained CPDAG

# Clear everything
rm(list=ls())

### Load required packages
##  Separate commands because some are large and the
##  download command may be slow or fail.
##  (However, if you re-run the commands it will not reload
##   packages that are already there.)
library("Rgraphviz")
library("RBGL")
library("abind")
library("corpcor")
library("sfsmisc")
library("robustbase")
library("pcalg")
library("graph")
plotcpdag <- "Rgraphviz" %in% print(.packages(lib.loc = .libPaths()[1]))

all_data <- read.csv("C:\\Users\\yiyangfan\\Desktop\\Spr2022\\STAT566\\proj\\brfss2020Simple.csv")
V <- colnames(all_data)
all_data <- all_data[V[2:dim(all_data)[2]]]
V <- colnames(all_data)
# Look at the data
all_data[1:10,]
str(all_data)
all_data = all_data[sample(dim(all_data)[1], dim(all_data)[1]),]

## The number of unique values of each variable:
ks = seq(1, 200000, 40000)
pcDAGS = c()
for (k in ks){
  data = all_data[seq(k, k + 40000, 1), ]

  t <- sapply(data, function(v) nlevels(as.factor(v)))
  t

  ## define sufficient statistics
  suffStat <- list(dm = data, nlev = t, adaptDF = FALSE)

  ## estimate CPDAG
  pc.DAG <- pc(suffStat,
           ## independence test: G^2 statistic
           indepTest = disCItest, alpha = 0.001, labels = V, verbose = TRUE)

  pcDAGS = c(pcDAGS, pc.DAG)
}

plot(pcDAGS[[1]], main = "Estimated CPDAG",labels=V)
plot(pcDAGS[[2]], main = "Estimated CPDAG",labels=V)
plot(pcDAGS[[3]], main = "Estimated CPDAG",labels=V)
plot(pcDAGS[[4]], main = "Estimated CPDAG",labels=V)
plot(pcDAGS[[5]], main = "Estimated CPDAG",labels=V)

save.image(file="C:\\Users\\yiyangfan\\Desktop\\Spr2022\\STAT566\\proj\\pcalg1.RData")

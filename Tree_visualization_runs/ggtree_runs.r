library("ggplot2")
library("ggtree")

tree <- treeio::read.nexus("Base_asr.tre")


ggtree(tree)
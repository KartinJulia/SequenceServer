library(ggplot2)

setwd('/Users/reetututeja/Documents/acic2019/hw8')

mydata= read.table("bmark1.txt",header = TRUE)

png(filename = 'plottime_bmark1.png',width = 800, height = 800)

ggplot(data=mydata, aes(x=mydata$size, y=mydata$time)) +
  geom_line() +
  geom_point() +
  xlab("DNA sequence length (bp)") + ylab("Time(sec)") +
  theme(legend.text=element_text(size=16)) +
  theme(axis.text=element_text(size=16),axis.title=element_text(size=16,face="bold"))

dev.off()

colortable <- `rownames<-`(cbind(t(col2rgb(colors()))/255,alpha=1),colors())
write.csv(colortable,"Rcolortable.csv")

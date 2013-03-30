setwd("/Users/vanilla_nadal/Desktop/")
data <- read.csv("step3.csv")
# Classify by gap number, count first
count_nodiff = 0
count_diff1 = 0
count_diff2 = 0
count_diff3 = 0
for (i in 1:512){
	if (data[i,2] - data[i,3] == 0){
		count_nodiff = count_nodiff  + 1;
	}
	else if (data[i,2] - data[i,3] == 1){
		count_diff1  = count_diff1  + 1;
	}
	else if (data[i,2] - data[i,3] == 2){
		count_diff2  = count_diff2  + 1;
	}
	else {
		count_diff3  = count_diff3  + 1;
	}
}
count_nodiff # 94
count_diff1 # 203
count_diff2 # 184
count_diff3 # 31
# Classify by gap number, put all in index.csv 
nodiff <- array(0, dim=c(203,1))
diff1 <- array(0, dim=c(203,1))
diff2 <- array(0, dim=c(203,1))
diff3 <-array(0, dim=c(203,1))
a = 1;
b = 1;
c = 1;
d = 1;
for (i in 1 : 512){
		if (data[i,2] - data[i,3] == 0){
			nodiff[a] = data[i,1];
			a = a + 1;
		}
		else if (data[i,2] - data[i,3] == 1){
			diff1[b] = data[i,1];
			b = b + 1;
		}
		else if (data[i,2] - data[i,3] == 2){
			diff2[c] = data[i,1];
			c = c + 1;
		}
		else {
			diff3[d] = data[i,1];
			d = d + 1;
		}		
}
nodiff
diff1
diff2
diff3
index <- cbind(nodiff, diff1, diff2, diff3)
colnames(index) = c("nodiff","diff1","diff2","diff3")
index[1:5,]
write.csv(index, "index.csv", row.names=FALSE)
# Retrieve the index with hole
hole <- array(0, dim=c(6,1))
e = 1
for (i in 1 : 512){
	if(data[i,5] == 1){
		hole[e] = data[i,1];
		e = e + 1;
	}
}
hole
# count total rectangles of each set
count_nodiff = 0
count_diff1 = 0
count_diff2 = 0
count_diff3 = 0
for (i in 1:512){
	if (data[i,2] - data[i,3] == 0){
		count_nodiff = count_nodiff  + data[i,2];
	}
	else if (data[i,2] - data[i,3] == 1){
		count_diff1  = count_diff1  + data[i,2];
	}
	else if (data[i,2] - data[i,3] == 2){
		count_diff2  = count_diff2  + data[i,2];
	}
	else {
		count_diff3  = count_diff3  + data[i,2];
	}
}
count_nodiff # 156
count_diff1 # 459
count_diff2 # 563
count_diff3 # 125
# count total rectangles by 0,1,2,3,4,5
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
for (i in 1:512){
	if (data[i,2] == 0){
		count_0 =  count_0 + 1;
	}
	else if (data[i,2] == 1){
		count_1 =  count_1 + 1;
	}	
	else if (data[i,2] == 2){
		count_2 =  count_2 + 1;
	}
	else if (data[i,2] == 3){
		count_3 =  count_3 + 1;
	}
	else if(data[i,2] == 4){
		count_4 =  count_4 + 1;
	}
	else{
		count_5 = count_5 + 1;
	}
}
count_0 # 1
count_1 # 36
count_2 # 201
count_3 # 232
count_4 # 41
count_5 # 1
# Put 
count_0 <- array(0, dim=c(232,1))
count_1 <- array(0, dim=c(232,1))
count_2 <- array(0, dim=c(232,1))
count_3 <- array(0, dim=c(232,1))
count_4 <- array(0, dim=c(232,1))
count_5 <- array(0, dim=c(232,1))
a = 1;
b = 1;
c = 1;
d = 1;
e = 1;
f = 1;
for (i in 1 : 512){
		if (data[i,2] == 0){
			count_0[a] = data[i,1];
			a = a + 1;
		}
		else if (data[i,2] == 1){
			count_1[b] = data[i,1];
			b = b + 1;
		}
		else if (data[i,2] == 2){
			count_2[c] = data[i,1];
			c = c + 1;
		}
		else if (data[i,2] == 3){
			count_3[d] = data[i,1];
			d = d + 1;
		}
		else if (data[i,2] == 4){
			count_4[e] = data[i,1];
			e = e + 1;
		}
		else{
			count_5[f] = data[i,1];
			f = f + 1;
		}		
}
count_0
count_1
count_2
count_3
count_4
count_5
rectangles <- cbind(count_0, count_1, count_2, count_3,count_4,count_5)
colnames(rectangles) = c("count_0","count_1","count_2","count_3","count_4","count_5")
rectangles[1:5,]
write.csv(rectangles, "rectangles.csv", row.names=FALSE)
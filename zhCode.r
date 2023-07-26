rm(list=1s0)#载入相关的R包
library(xgboost)
library(lubridate)
library(readx1)
drug_data <- read_excel("D:/R data/drug_data.x1sx")
view(drug_data)
drug_datasdate <- as.Date(drug_datasdate, format= "%Y/%m/%d")#将数据按照时间排序。
library(dplyr)drug_data <-drug_data %>% arrange(date)#创建 7ag 特征。
drug_data <- drug_data %>% mutate(lag1 = lag(ending_inventory, 1), lag2 = lag(ending_inventory, 2)) 
test <- drug_data %>% filter(date >= as.Date("2021-12-01"))#创建训练集和测试集。
train <- drug_data %>% filter(date < as.Date("2021-12-01"))#创建 xgboost 模型并进行训练。
model <- xgboost(data = as.matrix(train[, c("lag1", "lag2")]), label = trainsending_inventory, nrounds = 100, objective = "reg:squarederror") pred <- predict(model, as.matrix(test[, c("lag1", "lag2")]))#画图，进行数据可视化
par (mar=c(2,2,2,2))
y= testSending_inventory#如果想调节窗宽，用，ylim=c(min(10500),max(14000))
plot(testSdate, testSending inventory,type = "i", xlab = "date", ylab = "Drug Inventory",main = "Drug Inventory Time Series") 
legend("topleft", legend = c("Training Data", "Forecast"), col = c("black", "red"), 1ty = 1, cex = 0.8)
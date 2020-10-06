## Install finstr
#To install finstr from github use install_github from devtools package: 
library(devtools)
install_github("bergant/finstr")

library(dplyr)
library(tidyr)
library(finstr)
data(xbrl_data_aapl2013)
data(xbrl_data_aapl2014)

library(XBRL)
trace('XBRL', edit=TRUE)
# parse XBRL (Apple 10-K report)
xbrl_url2014 <- 
  "https://www.sec.gov/Archives/edgar/data/815097/000081509719000034/a3q201910-q_htm.xml"
xbrl_url2013 <- 
  "https://www.sec.gov/Archives/edgar/data/815097/000081509720000003/a2019form10-kfrontpart_htm.xml"
xbrl_data_aapl2014 <- xbrlDoAll(xbrl_url2014)
xbrl_data_aapl2013 <- xbrlDoAll(xbrl_url2013)
print(xbrl_data_aapl2014)


mtcars <- read.csv('updated_mtcars.csv')
print(aov(mpg ~ hp_level, data=mtcars))

#INSTALL "plotly" PACKAGE OF R IF NOT INSTALLED ALREADY USING --> install.packages("plotly")
library(plotly)

# custom grid style
axx <- list(
  gridcolor='rgb(255, 255, 255)',
  zerolinecolor='rgb(255, 255, 255)',
  showbackground=TRUE,
  backgroundcolor='rgb(230, 230,230)'
)

#INDIVIDUAL PLOTS 

#PLOT1 --> HISTOGRAM
hist <- plot_ly(iris, x=~Sepal.Length, type='histogram', scene='scene1') 
#TO SEE HISTOGRAM PLOT UNCOMMENT BELOW
#hist

#PLOT2 --> BOXPLOT
box_plot <- plot_ly(iris, y = ~Sepal.Length, type='box', color=~Species, scene='scene2')
#TO SEE BOX PLOT UNCOMMENT BELOW
#box_plot

#PLOT3 --> X-Y SCATTER PLOT
scatter_plot <- plot_ly(iris, x = ~Sepal.Length, y = ~Sepal.Width, type='scatter', mode='markers', scene='scene3')
#TO SEE SCATTER PLOT UNCOMMENT BELOW
#scatter_plot

#PLOT4 --> 3-D PLOT
plot_3d <- plot_ly(iris, x = ~Sepal.Length, y = ~Sepal.Width, z = ~Petal.Length, color = ~Species, colors = c('#BF382A', '#0C4B8E', '#8E880C'), scene='scene4')
plot_3d %>% layout(list(domain=list(x=c(0.5,1),y=c(0.5,1)),
                        xaxis=axx, yaxis=axx, zaxis=axx,
                        aspectmode='cube'))
#TO SEE 3-D PLOT UNCOMMENT BELOW
#plot_3d


#SUBPLOTTING TO CREATE A GRID OF 4-PLOTS ON A SINGLE WINDOW
fig1 <- subplot(hist, box_plot, scatter_plot, plot_3d, nrows=2)
fig1 <- fig1 %>% layout(title = "Data Plots :: IRIS Dataset",
                        scene1 = list(domain=list(x=c(0,0.5),y=c(0,0.5)),
                                      xaxis=axx, yaxis=axx,
                                      aspectmode='cube'),
                        scene2 = list(domain=list(x=c(0.5,1),y=c(0,0.5)),
                                      xaxis=axx, yaxis=axx,
                                      aspectmode='cube'),
                        scene3 = list(domain=list(x=c(0,0.5),y=c(0.5,1)),
                                      xaxis=axx, yaxis=axx,
                                      aspectmode='cube'),
                        scene4 = list(domain=list(x=c(0.5,1),y=c(0,0.5)),
                                      xaxis=axx, yaxis=axx, zaxis=axx,
                                      aspectmode='cube'))

#SHOW PLOT ON THE SCREEN
fig1


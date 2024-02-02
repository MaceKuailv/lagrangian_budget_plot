regen:
	jupyter execute figure3.ipynb --allow-errors &
	jupyter execute figure6.ipynb --allow-errors &
	jupyter execute boxplot.ipynb --allow-errors &
	jupyter execute contribution_plot.ipynb --allow-errors &
	jupyter execute freshmap.ipynb --allow-errors &
	jupyter execute hovmoller.ipynb --allow-errors &
	jupyter execute Mean_map.ipynb --allow-errors &
	jupyter execute saltymap.ipynb --allow-errors &
	jupyter execute contribution_map.ipynb --allow-errors &
	jupyter execute figure7.ipynb --allow-errors &
	jupyter execute line_plot.ipynb --allow-errors &
	jupyter execute neo_covariance.ipynb --allow-errors &
	jupyter execute table.ipynb --allow-errors &

xg:
	jupyter execute gen_xgyg.ipynb --allow-errors 
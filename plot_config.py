import matplotlib.pyplot as plt
import matplotlib as mpl
import cmocean
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.path as mpath

dpi = 100

projection = ccrs.LambertConformal(central_longitude=-45, central_latitude=58.0)
extent = (-95, 13, 12, 85)

depth_cmap = "Greys_r"
depth_norm = mpl.colors.Normalize(vmin=0, vmax=5000)

fresh_time_cmap = plt.get_cmap('BuPu_r')
fresh_theme_color = 'teal'

salty_time_cmap = plt.get_cmap('OrRd_r')
salty_theme_color = 'maroon'
salty_idate = 5479

mean_time_cmap = plt.get_cmap('YlGn_r')

a_palette5 = ["#df2935","#86ba90","#f5f3bb","#dfa06e","#412722"]
region_names =['gulf','labr','gdbk','nace','egrl']
region_colors = dict(zip(region_names,a_palette5))

rhs_list = ['e_ua','E','dif_h','dif_v','A','I','F']
term_colors = ['#66c2a5','#fc8d62','#8da0cb','#e78ac3','#a6d854','#ffd92f','#e5c494']
color_dic = dict(zip(rhs_list,term_colors))

balance = cmocean.cm.balance

term_dic = {
    'A': r"$-u'\cdot \nabla \bar s'$",
    'F': "Evap/Prec",
    'E': r"$(-u'\nabla s'-\overline{u'\nabla s'})$",
    # 'E': r"$\overline{u'\cdot \nabla s'}$",
    'dif_v': "Vertical Diffusion",
    'dif_h': "Horizontal diffusion",
    'e_ua': "Subdaily Advection",
    'I': "Surface salt flux and salt plume"
}

NUMBER_OF_PARTICLE_domain4 = 139968
NUMBER_OF_PARTICLE_domain_all = 1224905
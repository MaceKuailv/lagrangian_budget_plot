import matplotlib.pyplot as plt
import matplotlib as mpl
import cmocean
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.path as mpath

dpi = 100

projection = ccrs.LambertConformal(central_longitude=-45, central_latitude=58.0)
extent = (-95, 13, 12, 85)

balance = cmocean.cm.balance
depth_cmap = "Greys_r"
depth_norm = mpl.colors.Normalize(vmin=0, vmax=5000)

fresh_time_cmap = plt.get_cmap('BuPu_r')
fresh_theme_color = 'teal'
fresh_idate = 8918

salty_time_cmap = plt.get_cmap('OrRd_r')
salty_theme_color = 'maroon'
salty_idate = 5479

mean_time_cmap = plt.get_cmap('YlGn_r')

s_cmap = plt.get_cmap('PuOr_r')
term_cmap = balance

a_palette5 = ["#df2935","#86ba90","#f5f3bb","#dfa06e","#412722"]
region_names =['gulf','labr','gdbk','nace','egrl']
region_longnames = ['Gulf Stream','Labrador Current','Grand Bank','NAC Extension','East Greenland Current']
region_longnames = dict(zip(region_names, region_longnames))
region_colors = dict(zip(region_names,a_palette5))

# rhs_list = ['e_ua','E','dif_h','dif_v','A','I','F']
rhs_list = ['A','F','dif_v','dif_h','E','e_ua','I']
term_colors = ['#fc8d62','#66c2a5','#8da0cb','#e78ac3','#a6d854','#ffd92f','#e5c494']
color_dic = dict(zip(rhs_list,term_colors))

error_color = 'r'

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
case_term_dic = {
    'A': r"$-u'\cdot \nabla \bar s'$",
    'F': "Evap/Prec",
    # 'E': r"$(-u'\nabla s'-\overline{u'\nabla s'})$",
    'E': r"$\overline{u'\cdot \nabla s'}$",
    'dif_v': "Vertical Diffusion",
    'dif_h': "Horizontal diffusion",
    'e_ua': "Subdaily Advection",
    'I': "Surface salt flux and salt plume"
}

NUMBER_OF_PARTICLE_domain4 = 139968
NUMBER_OF_PARTICLE_domain_all = 1224905

TOTAL_VOLUME_salty,NUMBER_OF_PARTICLE_salty,VOLUME_EACH_salty = (269320135376896.0, 999984, 269324444.5680091)
TOTAL_VOLUME_fresh,NUMBER_OF_PARTICLE_fresh,VOLUME_EACH_fresh = (131811648733184.0, 1000041, 131806244.67715223)
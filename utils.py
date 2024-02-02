import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import os

def open_domain4():
    ds = xr.open_zarr('/sciserver/filedb08-03/ocean/wenrui_temp/rechunked_table_domain4')
    # path = '/sciserver/filedb10-01/ocean/wenrui_temp/table_domain5/'
    # slices = []
    # for i in range(5):
    #     slices.append(str(slice(i*730,(i+1)*730)))
    # subs = []
    # offsets = [i*730 for i in range(5)]
    # for slid in range(5): 
    #     strslice = slices[slid]
    #     sub_name = ['table'+str(i)+strslice for i in range(0,161)]
    #     datasets = [xr.open_zarr(path+name) for name in sub_name]
        
    #     sub = xr.concat(datasets,dim = 'time')
    
    #     sub['space']=sub.space+offsets[slid]
    #     subs.append(sub)
    # ds = xr.concat(subs,dim = 'space')
    return ds

def open_domain_all():
    ds = xr.open_zarr('/sciserver/filedb08-03/ocean/wenrui_temp/rechunked_table_domain_all')
    # path2 = '/sciserver/filedb10-02/ocean/wenrui_temp/table_domain_all/'
    # # print(len(os.listdir(path2))/161)
    
    # path1 = '/sciserver/filedb10-01/ocean/wenrui_temp/table_dec11/'
    
    # # import os
    # # print(len(os.listdir(path1)))
    
    # # print(len([i for i in os.listdir(path1) if 'slice(0' in i]))
    
    # # print(len([i for i in os.listdir(path1) if 'slice(7' in i]))
    
    # lst = os.listdir(path1)
    # proc = np.arange(0,161)
    # slices1 = [slice(0,730), slice(730,1095)]
    # for s in slices1:
    #     for p in proc:
    #         name = 'table'+str(p)+str(s)
    #         # if name not in lst:
    #         #     print(p, end = ' ')
    #     # print()
    # slices2 = []
    # for i in range(3,10):
    #     slices2.append(str(slice(i*365,(i+1)*365)))
    # slices2
    
    # subs = []
    # offsets = [(i+int(i>0.5))*365 for i in range(9)]
    # for slid in range(2):
    #     strslice = str(slices1[slid])
    #     sub_name = ['table'+str(i)+strslice for i in range(0,161)]
    #     datasets = [xr.open_zarr(path1+name) for name in sub_name]
    #     sub = xr.concat(datasets,dim = 'time')
    #     sub['space']=sub.space+offsets[slid]
    #     subs.append(sub)
    # for slid in range(3,10): 
    #     strslice = str(slices2[slid-3])
    #     sub_name = ['table'+str(i)+strslice for i in range(0,161)]
    #     datasets = [xr.open_zarr(path2+name) for name in sub_name]
    #     sub = xr.concat(datasets,dim = 'time')
    #     sub['space']=sub.space+offsets[slid-1]
    #     subs.append(sub)
    # ds = xr.concat(subs,dim = 'space')
    return ds

def open_case(which):
    if which == 'fresh':
        particle_path = '/sciserver/filedb04-01/ocean/wenrui_temp/particle_file/freshM/'
    elif which == 'salty':
        particle_path = '/sciserver/filedb08-01/ocean/wenrui_temp/particle_file/saltyM/'
    table_path = particle_path+'table/'
    map_path = particle_path+'maps/'
    maps = xr.open_zarr(map_path)
    table= xr.open_zarr(table_path)
    return maps, table

def open_case_month(which,int_arg):
    if which == 'fresh':
        those_slices = [427, 458, 486, 517]
        particle_path = '/sciserver/filedb04-01/ocean/wenrui_temp/particle_file/freshM/'
    elif which == 'salty':
        those_slices = [122,153,184,214,245,275,306]
        particle_path = '/sciserver/filedb08-01/ocean/wenrui_temp/particle_file/saltyM/'
    the_slice = slice(those_slices[int_arg], those_slices[int_arg+1])
    table_path = particle_path+str(the_slice)+'table/'
    map_path = particle_path+str(the_slice)+'maps/'
    maps = xr.open_zarr(map_path)
    table= xr.open_zarr(table_path)
    return maps, table

def open_monthly_mxld():
    mine = '/export/scratch/wjiang33/'
    mx = xr.open_zarr(mine+'mxd_monthly.zarr')
    return mx


def poly_from_xyrange(xrange,yrange):
    poly = []
    for x in xrange:
        for y in yrange:
            poly.append((x,y))
    poly = [poly[i] for i in [0,1,3,2]]
    return np.array(poly)
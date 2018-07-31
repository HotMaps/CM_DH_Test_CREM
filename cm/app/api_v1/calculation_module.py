
from osgeo import gdal




"""def calculation(file_name, factor, directory):
    ds = gdal.Open(file_name)
    ds_band = ds.GetRasterBand(1)

    #----------------------------------------------------
    pixel_values = ds.ReadAsArray()
    #----------Reduction factor----------------

    pixel_values_modified = pixel_values/ float(factor)
    indicator = pixel_values_modified.sum()
    gtiff_driver = gdal.GetDriverByName('GTiff')
    #print ()
    out_ds = gtiff_driver.Create(directory, ds_band.XSize, ds_band.YSize, 1, ds_band.DataType)
    out_ds.SetProjection(ds.GetProjection())
    out_ds.SetGeoTransform(ds.GetGeoTransform())

    out_ds_band = out_ds.GetRasterBand(1)
    out_ds_band.SetNoDataValue(0)
    out_ds_band.WriteArray(pixel_values_modified)

    del out_ds
    return indicator"""




import os
import sys
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.
                                                       abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
from my_calculation_module_directory.AD.F13_district_heating_potential.main import ad_f13
import my_calculation_module_directory.CM.CM_TUW4.run_cm as CM4



def calculation(heat_density_map, strd_vector, pix_threshold, DH_threshold, directory):
# TODO remove vector input the raster from GEO DB is already clipped by the user selection  => def calculation(file_path,heat_density_map, pix_threshold, DH_threshold, directory):
#
    #TODO  CM Base can HAndle only one Rasterfile as an output
    '''
    hdm in raster format from default dataset
    pix_threshold [GWh/km2]
    DH_threshold [GWh/a]
    potential level: NUTS0, 1, 2, 3, own shapefile
    '''
    #heat_density_map, strd_vector, pix_threshold, DH_threshold = ad_f13()
    '''
    
    Shapefile of NUTS0, 1, 2, 3 should be available in data warehouse; User
    should also be able to calculate potential for the selected area: shall
    be considered in AD
    Outputs:
        DH_Regions: contains binary values (no units) showing coherent areas
        clipped_hdm: hdm after clipping [MWh/ha]
        rasterOrigin: Top-left corner of raster array
    '''

    output_dir = path + os.sep + 'Outputs' # TODO remove this Lines there will be only one files as an output
    outRasterPath, outShapefile = CM4.main(heat_density_map, strd_vector,
                                           pix_threshold, DH_threshold,
                                           output_dir)
    return {'F13_out_raster_path_0': outRasterPath,
            'F13_out_shapefile_path_0': outShapefile}


""" if __name__ == "__main__":
    output_dir = path + os.sep + 'Outputs'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    output = calculation(output_dir)
    print(output)"""

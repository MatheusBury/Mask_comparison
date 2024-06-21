# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:56:16 2023

@author: Bury
"""

import os
import shutil


def create_folder(folder):
    if not os.path.exists(folder):

        os.mkdir(folder)
        #print(f'Folder Criado {folder}')

root = r'C:\Users\Operacao\Downloads\mv31_murphy_equinor_red\alt_predictions_IA Send 18_06_2024'
output_folder = f'{root}_comparison'


create_folder(output_folder)



for folder in os.listdir(root):
    
    folders = os.path.join(root,folder)
    #print(folders)
    
    

    for image in os.listdir(folders):

        folder_name = os.path.join(root,folder)

        create_folder(os.path.join(output_folder,folder))

        sub_output_folder = os.path.join(output_folder,folder)

        print(sub_output_folder)

        original = f'{folder_name}\{image}\img.jpg'
        shutil.copyfile(original, f'{sub_output_folder}\{image}.jpg')

        murphy_236pm_equinor_red = f'{folder_name}\{image}\pred_unet_experimental_vsp_murphy_04252024_236pm_filter_by_version_all_imgs_equinor_red.jpg'
        shutil.copyfile(murphy_236pm_equinor_red, f'{sub_output_folder}\{image}_murphy_236pm_equinor_red.jpg')

        murphy_236pm_equinor_red_2 = f'{folder_name}\{image}\pred_unet_experimental_vsp_murphy_04252024_236pm_filter_by_version_all_imgs_equinor_red2.jpg'
        shutil.copyfile(murphy_236pm_equinor_red_2, f'{sub_output_folder}\{image}_murphy_236pm_equinor_red_(2).jpg')

        pred_bai_1495_murphy = f'{folder_name}\{image}\pred_bai_1495_murphy.jpg'
        shutil.copyfile(pred_bai_1495_murphy, f'{sub_output_folder}\{image}_bai_1495_murphy.jpg')

        pred_bai1495_0 = f'{folder_name}\{image}\pred_bai1495_0.jpg'
        shutil.copyfile(pred_bai1495_0, f'{sub_output_folder}\{image}_bai1495_0.jpg')

        pred_modec_mv30 = f'{folder_name}\{image}\pred_modec_mv30.jpg'
        shutil.copyfile(pred_modec_mv30, f'{sub_output_folder}\{image}_modec_mv30.jpg')

        pred_unet_9m = f'{folder_name}\{image}\pred_unet_9m.jpg'
        shutil.copyfile(pred_unet_9m, f'{sub_output_folder}\{image}_unet_9m.jpg')

        pred_unet_altera_0_ = f'{folder_name}\{image}\pred_unet_altera_0_.jpg'
        shutil.copyfile(pred_unet_altera_0_, f'{sub_output_folder}\{image}_unet_altera_0_.jpg')

        pred_unet_equinor_red_ = f'{folder_name}\{image}\pred_unet_equinor_red_.jpg'
        shutil.copyfile(pred_unet_equinor_red_, f'{sub_output_folder}\{image}_unet_equinor_red_.jpg')

        pred_unet_equinor1_0_ = f'{folder_name}\{image}\pred_unet_equinor1_0_.jpg'
        shutil.copyfile(pred_unet_equinor1_0_, f'{sub_output_folder}\{image}_unet_equinor1_0_.jpg')

        pred_unet_equinor2_0_ = f'{folder_name}\{image}\pred_unet_equinor2_0_.jpg'
        shutil.copyfile(pred_unet_equinor2_0_, f'{sub_output_folder}\{image}_unet_equinor2_0_.jpg')

        pred_unet_modec_0_ = f'{folder_name}\{image}\pred_unet_modec_0_.jpg'
        shutil.copyfile(pred_unet_modec_0_, f'{sub_output_folder}\{image}_unet_modec_0_.jpg')

        pred_unified = f'{folder_name}\{image}\pred_unified.jpg'
        shutil.copyfile(pred_unified, f'{sub_output_folder}\{image}_unified.jpg')




        
    print('Finalizado..')
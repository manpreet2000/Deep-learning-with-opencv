#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[6]:


def orderd_points(points):
    
    """To convert points in orders form this function is called
         first point----- top left
         second point ----top right
         third point -----bottom right
         fourth point-----bottom left"""
    orderd=np.zeros((4,2),dtype="float32")
    """ top left have minimum sum (x+y) and bottom right will have 
    max sum (x+y) """
    s=points.sum(axis=1)
    orderd[0]=points[np.argmin(s)]
    orderd[2]=points[np.argmax(s)]
    
    """ top right have minimum difference (x-y) and bottom left will have 
    max difference (x+y) """
    
    s=np.diff(points,axis=1)
    orderd[1]=points[np.argmin(s)]
    orderd[3]=points[np.argmax(s)]
    
    return orderd
    
    
    


# In[13]:


def four_points(img,points):
    orderd=orderd_points(points)
    """we need to find width and height so, width will be max of distance b/w top (left and top right)
    and (bottom left and bottom right) 
    height will be max of (tl,bl) and (tr,br) """
    
    (tl,tr,br,bl)=orderd
    
    wa=np.sqrt(((tl[0]-tr[0])**2)+((tl[1]-tr[1])**2))
    wb=np.sqrt(((bl[0]-br[0])**2)+((bl[1]+br[1])**2))
    maxWidth=max(int(wa),int(wb))
    
    
    ha=np.sqrt(((tr[0]-br[0])**2)+((tr[1]-br[1])**2))
    hb=np.sqrt(((tl[0]-bl[0])**2)+((tl[1]+bl[1])**2))
    maxHeight=max(int(ha),int(hb))

    
    dst = np.array([[0, 0],[maxWidth - 1, 0],[maxWidth - 1, maxHeight - 1],[0, maxHeight - 1]], dtype = "float32")
    
    M = cv2.getPerspectiveTransform(orderd, dst)
    warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))
    
    return warped
    
    


# In[ ]:





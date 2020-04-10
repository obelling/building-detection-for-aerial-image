import os
import cv2 as cv
import numpy as np
from PIL import Image
class ImgPre:
    def __init__(self, rootPath, export_path_base):
        self.rootPath = rootPath
        self.export_path_base = export_path_base

        try:
            if not os.path.exists(export_path_base):
                os.mkdir(export_path_base)
        except Exception as e:
            print("loading error.......")

    def get_savename(self,operate):
        try:
            import time
            now = time.time()
            tail_time = str(round(now*1000000))[-4:]
            head_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            label = str(head_time+tail_time)
            label = str(head_time+tail_time)
            export_path_base = self.export_path_base
            out_path = export_path_base+operate
            if not os.path.exists(out_path):
                os.mkdir(out_path)
            savename = out_path+'/'+operate+'_'+label+'.jpg'

            return savename
        except Exception as e:
            print("save error......")
    def transpose(self):
        try:
            operate = 'transpose'
            rootPath = self.rootPath

            list =os.listdir(rootPath)
            for files in list:
                img = cv.imread(os.path.join(rootPath,files))
                dst = cv.flip(img,-1)
                cv.imwrite(os.path.join(self.export_path_base,files),dst)
        except Exception as e:
            print('ERROR %s',operate)

    def rotate(self,angle):
        try:
            operate = 'rotate_'+str(angle)
            rootPath = self.rootPath

            list = os.listdir(rootPath)
            for files in list:
                img = cv.imread(os.path.join(rootPath,files))
                (h,w) = img.shape[:2]
                (cx,cy) = (w/2,h/2)
                M = cv.getRotationMatrix2D((cx,cy),angle,1.0)
                cos = np.abs(M[0,0])
                sin = np.abs(M[0,1])
                #计算新边界
                nw = int(h*sin+w*cos)
                nh = int(h*cos+w*sin)
                #调整移动距离
                M[0,2] +=(nw/2)-cx
                M[1,2] +=(nh/2)-cy

                dst = cv.warpAffine(img,M,(nw,nh))
                #savename = self.get_savename(operate)
                cv.imwrite(os.path.join(self.export_path_base,operate+str(files)),dst)
        except Exception as e:
            print('SAVE ERROR......')
def test():
    rootPath = 'D:/CODE/Faster-RCNN-TensorFlow-Python3-master/data/VOCdevkit2007/VOC2007/JPEGImages/'
    export_path_base = 'D:/CODE/Faster-RCNN-TensorFlow-Python3-master/data/VOCdevkit2007/VOC2007/export/'
    # 声明类对象
    imgPre = ImgPre(rootPath, export_path_base)

    #imgPre.transpose()
    imgPre.rotate(15)
    imgPre.rotate(30)

if __name__ =='__main__':
    import datetime
    print('start...')

    test()

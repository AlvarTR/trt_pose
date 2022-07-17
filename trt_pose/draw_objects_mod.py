import cv2


class DrawObjects(object):

    def __init__(self, topology):
        self.topology = topology

    def __call__(self, image, object_counts, objects, normalized_peaks):
        topology = self.topology
        #height = image.shape[0]
        #width = image.shape[1]
        size = tuple(image.shape[1:-1:-1])
        color = (0, 255, 0)

        #K = topology.shape[0]
        #count = int(object_counts[0])
        #K = topology.shape[0]
        #for i in range(count):
        #    obj = objects[0][i]
        for obj in objects[0]:
            #C = obj.shape[0]
            #for j in range(obj.shape[0]):
            #    k = int(obj[j])
            for i, objInt in enumerate(map(int, obj)):
                #if k >= 0:
                if objInt < 0:
                    continue
                peaks = normalized_peaks[0][i][objInt][::-1]
                #x = round(float(peak[1]) * width)
                #y = round(float(peak[0]) * height)
                coor = ( round(float(p*s)) for p, s in zip(peaks, size) )
                #cv2.circle(image, (x, y), 3, color, 2)
                cv2.circle(image, coor[::-1], 3, color, 2)

            #for k in range(topology.shape[0]): #range(K)
            for indexes in topology[:][2:4]:
                #c_a = topology[k][2]
                #c_b = topology[k][3]
                #if obj[c_a] >= 0 and obj[c_b] >= 0:
                #if obj[c_a] < 0:
                #    continue
                #if obj[c_b] < 0:
                #    continue
                #if any(i < 0 for i in indexes):
                #    continue
                #peak0 = normalized_peaks[0][c_a][obj[c_a]]
                #peak1 = normalized_peaks[0][c_b][obj[c_b]]
                peaks = tuple( normalized_peaks[0][i][obj[i]][:][::-1] for i in indexes if i >= 0)

                #x0 = round(float(peak0[1]) * width)
                #y0 = round(float(peak0[0]) * height)
                coor0 = ( round(float(p*s)) for p, s in zip(peaks[0], size) )

                #x1 = round(float(peak1[1]) * width)
                #y1 = round(float(peak1[0]) * height)
                coor1 = ( round(float(p*s)) for p, s in zip(peaks[1], size) )

                #cv2.line(image, (x0, y0), (x1, y1), color, 2)
                cv2.line(image, coor0, coor1, color, 2)

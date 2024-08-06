from mmsdk import mmdatasdk


cmumosi_highlevel=mmdatasdk.mmdataset(mmdatasdk.cmu_mosi.highlevel,'cmumosi/')
cmumosi_highlevel.add_computational_sequences(mmdatasdk.cmu_mosi.labels,'cmumosi/')
cmumosi_highlevel.align('Opinion Segment Labels')

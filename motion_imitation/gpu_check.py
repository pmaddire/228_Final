import tensorflow as tf

# TF 1.x compatible GPU check
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
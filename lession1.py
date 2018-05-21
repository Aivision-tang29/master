import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
sess = tf.Session()
writer = tf.summary.FileWriter('./graphs', sess.graph)
print(sess.run(x))
writer.close()

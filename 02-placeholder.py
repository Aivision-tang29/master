import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

###EXP1: placeholder with a feed_dict

a = tf.placeholder(tf.float32, shape=[3])
b = tf.constant([5, 5, 5], tf.float32)

c = a + b
writer = tf.summary.FileWriter('./graphs/placeholder', tf.get_default_graph())
with tf.Session() as sess:
    print(sess.run(c, feed_dict={a: [1, 2, 3]}))
writer.close()


##Exp2:  a variable feed_dict
a = tf.add(2, 5)
b = tf.multiply(a, 3)

writer = tf.summary.FileWriter('./graphs/feeddict', tf.get_default_graph())
with tf.Session() as sess:
    print(sess.run(b))
    print(sess.run(b, feed_dict={a: 15}))
writer.close()

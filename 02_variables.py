import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np

# Example 1: creating variables
# s = tf.Variable(2, name="scalar")
# m = tf.Variable([1, 2], [3, 4], name="matrix")
# w = tf.Variable(tf.zeros([784, 10]), name="big matrix")
# v = tf.Variable(tf.truncated_normal([784, 10], name="normal matrix"))
# tf.InteractiveSession()
# s = tf.get_variable('scalar', initializer=tf.constant(2))
# m = tf.get_variable('matrix', initializer=tf.constant([[1, 2], [3, 4]]))
# w = tf.get_variable('big_matrix', shape=(784, 10), initializer=tf.zeros_initializer())
# v = tf.get_variable('normal_matrix', shape=(784, 10), initializer=tf.truncated_normal_initializer())
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(v.eval())


# Example 2: assigning values to variables
# w=tf.Variable(10)
# # w.assign(100)
# # with tf.Session() as sess:
# #     print(sess.run(w.initializer))
# #     print(sess.run(w))
#
# assign_op=w.assign(100)
# with tf.Session() as sess:
#     print(sess.run(assign_op))
#     print(sess.run(w))

# # create a variable whose original value is 2
# a = tf.get_variable('a', initializer=tf.constant(2))
# atimes2 = a.assign(a * 2)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(atimes2))
#     print(sess.run(atimes2))
#     print(sess.run(atimes2))
#     print(sess.run(atimes2))
#
# w = tf.Variable(10)
# with tf.Session() as sess:
#     sess.run(w.initializer)
#     print(sess.run(w.assign(20)))
#     print(sess.run(w.assign_sub(2)))

# Example 3: Each session has its own copy of variable
W = tf.Variable(10)
sess1 = tf.Session()
sess2 = tf.Session()
sess1.run(W.initializer)
sess2.run(W.initializer)
print(sess1.run(W.assign_add(10)))
print(sess2.run(W.assign_sub(2)))
print(sess1.run(W.assign_add(100)))
print(sess2.run(W.assign_sub(50)))
sess1.close()
sess2.close()

w = tf.Variable(tf.truncated_normal([784, 10]))
u = tf.Variable(w * 2)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(w))
    print(sess.run(u))

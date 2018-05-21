import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# ##########Exp1  : a simple way to create log file writer
#
# a = tf.constant(1, name='a')
# b = tf.constant(2, name='b')
# x = tf.add(a, b, name='x')
# writer = tf.summary.FileWriter('./graphs/simple', tf.get_default_graph())
# with tf.Session() as sess:
#     print(sess.run(x))
# writer.close()

# # Example 2: The wonderful wizard of div
# a = tf.constant([2, 2], name="a")
# b = tf.constant([[0, 1], [2, 3]], name="b")
# with tf.Session() as sess:
#     print(sess.run(tf.div(b, a)))
#     print(sess.run(tf.divide(b, a)))#xiaoshu
#     print(sess.run(tf.truediv(b, a)))##
#     print(sess.run(tf.floordiv(b, a)))
#     print(sess.run(tf.truncatediv(b, a)))
#     print(sess.run(tf.floor_div(b, a)))

# # Example 3: multiplying tensors
# a = tf.constant([10, 20], name="a")
# b = tf.constant([2, 3], name="b")
#
# with tf.Session() as sess:
#     print(sess.run(tf.multiply(a, b)))#####[20,60]
#     print(sess.run(tf.tensordot(a, b,1)))####80


# Example 4: Python native type
# sess = tf.Session()
# t_0 = 19
# x = tf.zeros_like(t_0)
# y = tf.ones_like(t_0)
# print(sess.run(x), sess.run(y))

# t_1 = ['apple', 'peach', 'banana']
# x = tf.zeros_like(t_1)
# y = tf.ones_like(t_1)
# print(x)

# t_2 = [[True, False, False],
#        [False, False, True],
#        [False, True, False]]
# x = tf.zeros_like(t_2)
# y = tf.ones_like(t_2)
# print(sess.run(x),sess.run(y))
#
# print(tf.int32.as_numpy_dtype())

# Example 5: printing your graph's definition

my_constant = tf.constant([15, 30], name="my_constant")
print(tf.get_default_graph().as_graph_def())

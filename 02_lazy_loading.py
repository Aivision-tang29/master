import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

################################
####Normal      loading#########
####print a grpah with 1 add node###
################################

x = tf.Variable(10, name='X')
y = tf.Variable(20, name='Y')
z = tf.add(x, y)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer=tf.summary.FileWriter('./graphs/normal_loading',sess.graph)
    for _ in range(10):
        sess.run(z)
    print(tf.get_default_graph().as_graph_def())
    writer.close()

# ################################
# ####    lazy  loading#########
# ####print a grpah with 10 add node###
# ################################

x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/lazy_loading', sess.graph)
    for _ in range(10):
        sess.run(tf.add(x, y))
    print(tf.get_default_graph().as_graph_def())
    writer.close()

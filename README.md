# fraud-detection-self-organizing-maps

Overview: 
1. Intuition of Self Organizing Maps (SOMs)
2. How to build a SOM
3. How to return the specific features (like frauds) detected by the SOM
4. How to make Hybrid Deep Learning Model

Plan of Attack
1. How do Self-Organizing Maps Work?
   - They're one of the simplest algorithms
2. K-Means Clustering 
3. How do Self-Organizing Maps Learn?
4. SOM structure itself, and perserves correlation and similarity in dataset, portrays them in a lower-dimesionality representation which is your 2-D map.
5. Reading an Advanced SOM

### How do SOMs work? 
- Already covered the following:
  - Supervised Deep Learning
    - Artificial Neural Networks (Used for Regression and Classification)
    - Convolutional Neural Networks (Used for Computer Vision)
    - Recurrent Neural Networks (Used for Time Series Analysis) 
- Moving onto Unsupervised Deep Learning
  - Unsupervised Deep Learning
    - Self-Organizing Maps (Used for Feature Detection)
    - Deep Boltzmann Machines (Used for Recommendation Systems)
    - AutoEncoders (Used for Recommendation Systems) 
- Self-Organizing Maps
  - Invented in the 1980s
  - SOMs are used for reducing dimensionality 
    - Example: SOM for Astronomy -> Visualization, take a multi-dimensional dataset with lots and lots of columns (the dimensions of the dataset) and lots of rows, and reduce the dimensionality (from 100 - 300 columns to a map)
    - Results in a Two-Dimensional Representation of your dataset
    - Purpose of SOMs is to reduce the number of columns
  - E.g. clusters of indicator (39 parameters, quality of life, factors, state of health, etc. huge dataset of 200+ countries) 
  - Multi-dimensional dataset into two dimensions
  - SOM can reduce into a map
  - Unsupervised Learning -> has training data but no labels in the training data. Not like a CNN where it learns what it's seeing and then apply that to the test data. Unsupervised it's given a lots of data and learns to group these datas (it didn't learn for example that Belgium, Sweden, Japan should be grouped together but rather that ah they have similar datasets based on all of the indicators looking at) similarity - learned on its own. 
    - We can put the example on the world map. 
    - Data (lots of columns) => SOM => Visualization 
  - Additional Reading: Self-organizing map -> https://pdfs.semanticscholar.org/7403/57022426b93b607ea782715c63479f4f8c41.pdf

### Revisiting K-Means Clustering
- Before K-Means 
- After K-Means
- Prepare you for SOM, process of pushing and pulling as the centroids by the actual datapoints. 
- K-Means is unsupervised machine learning algorithm

### K-Means Intuition: Understanding K-Means
- Algorithm to cluster your data, discovering categories in dataset you wouldn't find yourself
- Scatterplot (Before K-Means), plot X&Y
- identify the groups itself, K-Means => Clusters of data in dataset
- Can work with multi-dimensional objects
- How did it do that?
   - Step 1: Choose the numebr K of clusters 
   - Step 2: Select at random K points, the centroids (not necessairly from your dataset) 
   - Step 3: Assign each data point to the closest centroid => that forms K clusters
   - Step 4: Compute the place the new centroid of each cluster
   - Step 5: Reassign each data point to the new closest centroid. If any reassignment took place, go to Step 4, otherwise go to FINISH
   - Model is Ready
- Example
   - Step 1: K = 2
   - Actual points or random points
   - Assign each data point to the closest centroid => forms K clusters
   - perpindicular line, any point on green line is equidistant, euclidean distances (e.g.)
   - Reassign each data point to the new closest centroid. If any reassignment took place  
### How do SOMs Learn?
- E.g. three features in our input vectors, nine nodes in output
- SOMs used to reduce dimensionality of the dataset, 
- Three features => Columns, thousands of thousands rows
- SOMs output is always 2D
- SOMs familiar to us ANN, RNN, CNN
   - Same network, only difference is the position of the nodes
   - SOMs are very different from supervised neural networks
      - 1) Much much easier than ANN, simple and straightforward
      - 2) Concepts that have the same name, but different meaning, might confuse meanings
   - Three synapases to the top output node (weight assigned, w1.1, w1.2, w1.3) 
   - Weights have a different connotation than ANN, in ANN weights were used to multiply the input by the weight added up and applied an activation function
   - No activation function in SOMs
   - Weights are a characteristics of the node itself, node has coordinates
   - Node like a ghost in our input space, where it can fit, weights are the coordinates of the node in the input space
   - Each is a ghost or an imaginary data point, trying to blend in
   - Has its own weights at the start of the algorithm
   - So why is this important, core of the self-organizing map algorithm
   - rows which of these nodes is closets to our rows in our dataset
   - competition -> every node which is the closest to our input state - euclidean distance, get values close to 1 (0 and 1 input, normalization or standardization) 
   - Row #1 to each node, BMU (Best Matching Unit) the closest -> core of the SOM algorithm
   - What happens next?
      - Found BMU, SOM will update 'weights' - weights are characteristic of nodes in SOM, even closer to our first row in our data set
      - SOM is coming closer to the datapoint, drag the SOM closer to the point
      - Self-organizes onto input data, some of the nearby points are being dragged closer to this point
      - COme closer to the row that they matched up to, closer to BMu heavier weights of data, weights are updated less
   - Whole chain, whole structure same direction, harder pulled BMU matched up with, radius concept works
   - How do they fight with each other? (Green BMU, Blue BMU, Red BMU) -> pulled much harder and becomes, greenish blue, pull on green and blue, both have an impact
### How do SOMs Learn Pt.2
   - Best Matching Units (BMUs) are updated
   - Sophisticated example (5 BMUs)
   - BMUs updated even closer to row they matched up to, area around it radius, radius selected at beginning is usually - nodes are updated
   - Purple node (row that is matched up), dragged closer and closer - resistance push and pull, new epoch, unique KOHONAN learning algorthm
   - radius starts shrinking through the algorithm - pulling on nodes, radius is shrinked, nodes are pulled - process becomes more and more accurate, more and more iterations (precise, more laser specific manner), mask for your data
   - battle between different nodes, settled into some kind of representation
   - Takeaways from the tutorial:
      - 1) SOMs retain topology of the input set - does everything it can to be as close to the data, like a mask for dataset, understanding datasets better
      - 2) SOMs reveal correlations that are not easily identified SOMs can neatly put all anyalze into a mso, see into map easily
      - 3) SOMs classify data without supervision - don't actually need labels (CNNs => train our dataset to recognize objects, after lots and lots of iterations - don't need any labels - SOMs will extract feature or show us dependencies and correlation not expecting) - used in scenarios you don't know what you're looking for
      - 4) No target vector -> no backpropagation - unsupervised, we don't actually have a target vector, no lateral connection between output nodes, pull on one node other gets pulled, radius we outline
      - 5) No Neural Network - output, there's a grid behind, are indeed on a self-organizing map
   - Soft math on SOMs => http://ai-junkie.com/ann/som/som1.html 
- Live Example of SOMs
   - Inputs of eight colors (Red, green, blue, orange, yellow, purple, RGB code for each color)
   - From 0 to 1, 8 rows, three columns into SOMs
   - Starting weights at random, dark blue (perserve topology) 
   - Very simple SOM in action

### How to read an Advanced SOM
   - Voting patterns in the U.S. Congress
   - Example of Wikipedia, voting results of voting patterns of U.S. Congress - members of congress, over 535 members, 100 senators, which members of congress are similar to each and which are disimilar
   - See results and visual overlay with the original cluster 
   - Why is there a yellow spot in the middle, overlaid, not a 1-to-1 representation was voting as a yes
   - https://www.visualcinnamon.com/2013/07/self-organizing-maps-creating-hexagonal.html
   

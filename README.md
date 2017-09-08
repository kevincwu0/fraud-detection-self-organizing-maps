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

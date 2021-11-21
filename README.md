# Custom Python Modules
A set of custom Python modules created by me for various tasks and applications.

---
## Contents
- [data_visualization.py](data_visualizationpy) : For data visualization of NN models using matplotlib.
- [linked_list.py](linked_listpy) : For creating and modifying linked lists.
- [one_hot_characters.py](one_hot_characterspy) : For encoding and decoding strings into and from a tensor of one-hot tensors.
---
## Modules:
### data_visualization.py
Used to visualize data gathered during and after NN model training/testing using matplotlib. 


- **create_acc_loss_plot()** : Plots acc, val_acc in one plot and loss, val_loss in another in one figure. Used for overfitting check.


### linked_list.py
Used to create and modify singly-linked lists.

- **Node** : Create a new linked list node with a data field and next field.
- **create_list** : Create a linked list with an array.
- **insert_at_start** : Insert node to start of linked list.
- **insert_at_end** : Insert node to end of linked list.
- **remove_at** : Remove node at given index.
- **insert_at** : Insert node at given index.
- **remove** : Remove node with given value (data).
- **insert_after** : Insert node after the node that contains the given value (data).
- **get_length** : Get length of linked list.
- **print** : Print linked list.

### one_hot_characters.py
Used to convert any string into a PyTorch tensor of one-hot tensors and vice versa. The following languages are supported; "eng".

- **create_dict** : Create dictionary for the selected language with integer values assigned to each character.
- **encode_str** : Create a tensor of one-hot tensors from a given string.
- **decode_str** : Create a string using a given tensor of one-hot tensors.


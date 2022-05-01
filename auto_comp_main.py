# Import Modules
import nuke


def shuffle_layer(node, layer):
    """
    Create a shuffle node from the "node" with given "layer"
    :param node: Input node for shuffle
    :param layer: Layer to be shuffled out
    :return: Shuffle node
    """

    shuffle_node = nuke.nodes.Shuffle(label=layer, inputs=[node])
    shuffle_node["in"].setValue(layer)
    shuffle_node["postage_stamp"].setValue(True)

    return shuffle_node


def select_all_upstream(node):
    """
    Recursive function selecting all nodes upstream
    :param node: starting node for selection
    :return: Will return when no further nodes upstream
    """
    if not node.dependencies():
        return

    node.setSelected(True)
    deps = node.dependencies()

    for d in deps:
        d.setSelected(True)
        if not node.dependencies():
            continue
        select_all_upstream(node=d)


def space_nodes(scale):
    """
    Space out node tree in the Y axis
    :param scale: Unit value for separation
    """
    nodes = nuke.selectedNodes()  # Get Selected Nodes
    amount = len(nodes)

    # Sum of X & Y values
    all_x = sum([n.xpos() + n.screenWidth() / 2 for n in nodes])
    all_y = sum([n.ypos() + n.screenHeight() / 2 for n in nodes])

    # Center pivot pos of all nodes
    center_x = all_x / amount
    center_y = all_y / amount

    # Reposition Nodes from center pivot
    for n in nodes:
        n.setYpos(center_y + (n.ypos() - center_y) * scale)


def auto_comp():
    """
    Split node into layers based on "Group"
    :return:
    """
    selected_node = nuke.selectedNode()

    # Get all channels
    channels = selected_node.channels()
    layers = [c.split('.')[0] for c in channels]

    # Remove Duplicates from layers
    layers = list(set([c.split('.')[0] for c in channels]))
    layers.sort()

    # Create panel to map AOVs
    p = nuke.Panel("Map AOVs")
    p.addSingleLineInput("Group", "lgt")
    p.addEnumerationPulldown("depth", ' '.join(channels))
    p.addBooleanCheckBox("invert depth", False)

    if not p.show():
        return

    # Store panel results
    group = p.value("Group")
    depth = p.value("depth")
    invert_z = p.value("invert depth")

    # Create starting dots
    root_dot = nuke.nodes.Dot(inputs=[selected_node])
    rgb_dot = nuke.nodes.Dot(inputs=[root_dot])

    # Isolate layers base on group result
    group_layers = []

    for layer in layers:
        if group in layer:
            group_layers.append(layer)

    # Create Shuffle nodes
    shuffle_node_list = []

    for idx, layer in enumerate(group_layers):
        idx = shuffle_layer(root_dot, layer)
        shuffle_node_list.append(idx)

    # Connect merge nodes
    previous_node = None

    for idx, node in enumerate(shuffle_node_list):
        current_node = nuke.nodes.Grade(inputs=[node])
        if idx == 0:
            start_dot = nuke.nodes.Dot(inputs=[current_node])
            previous_node = start_dot
        else:
            merge = nuke.nodes.Merge2(operation="plus", inputs=[previous_node, current_node], output="rgb")
            previous_node = merge

    # Add depth grading nodes
    if invert_z:
        result = nuke.nodes.Invert(channels=depth, inputs=[previous_node])
    else:
        result = previous_node

    g = nuke.nodes.Grade(inputs=[result])
    g['black'].setValue(0.05)
    g['mask'].setValue(depth)

    # Fix bug for rgb dot tree position
    x_pos = rgb_dot.xpos()
    rgb_dot['xpos'].setValue(x_pos)

    # Copy alpha and pre-multiply
    copy_node = nuke.nodes.Copy(from0="rgba.alpha", to0="rgba.alpha")
    copy_node.setInput(0, g)
    copy_node.setInput(1, rgb_dot)
    copy_node['xpos'].setValue(selected_node.xpos())
    copy_node['ypos'].setValue(g.ypos())

    premult_node = nuke.nodes.Premult(inputs=[copy_node])

    # Reposition nodes
    select_all_upstream(premult_node)
    space_nodes(3)





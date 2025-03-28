import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# Define the main process steps
steps = [
    "User Input Processing",
    "Tokenization & NLP Analysis",
    "Intent Classification",
    "Entity Recognition",
    "Knowledge Base Retrieval",
    "Response Generation",
    "Learning & Improvement"
]

# Define associated ML techniques for each step (displayed on the side)
ml_components = [
    ["Text cleaning","Normalization"],
    ["Tokenization","POS tagging","Semantic analysis"],
    ["ML classifiers","Intent categorization"],
    ["NER models","Entity extraction"],
    ["Vector embeddings","RAG","Semantic search"],
    ["LLMs","NLG","Personalization"],
    ["Feedback loop","Model retraining"]
]

# Create figure
fig,ax = plt.subplots(figsize=(7,10))
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.axis('off')

# Colors
main_color = "#3498db"
secondary_color = "#2980b9"
text_color = "#ffffff"
line_color = "#34495e"
component_color = "#e8f4fc"
component_border = "#7fb3d5"

# Draw the main process steps (vertical flow)
box_width = 3.1
box_height = 0.5
main_x = 3.5
spacing = 1.4
y_positions = []

for i,step in enumerate(steps) :
    y_pos = 9 - i * spacing
    y_positions.append(y_pos)

    # Add main process box
    box = FancyBboxPatch(
        (main_x,y_pos - box_height / 2),
        box_width,box_height,
        boxstyle="round,pad=0.2",
        facecolor=main_color if i % 2 == 0 else secondary_color,
        edgecolor=line_color,
        linewidth=0.8
    )
    ax.add_patch(box)

    # Add step number and text
    ax.text(main_x + 0.2,y_pos,f"{i + 1}",
            fontsize=10,fontweight='bold',color=text_color,
            va='center')
    ax.text(main_x + 0.6,y_pos,step,
            fontsize=9,color=text_color,
            va='center')

    # Add ML components on the right side
    component_x = main_x + box_width + 0.4
    component_width = 2.2
    component_height = 0.2
    component_spacing = 0.5

    # Determine vertical positioning of components
    num_components = len(ml_components[i])
    total_height = num_components * component_height + (num_components - 1) * 0.1
    start_y = y_pos + total_height / 2 - component_height / 2

    for j,component in enumerate(ml_components[i]) :
        comp_y = start_y - j * component_spacing

        # Add component box
        comp_box = FancyBboxPatch(
            (component_x,comp_y - component_height / 2),
            component_width,component_height,
            boxstyle="round,pad=0.1",
            facecolor=component_color,
            edgecolor=component_border,
            linewidth=0.8
        )
        ax.add_patch(comp_box)

        # Add component text
        ax.text(component_x + component_width / 2,comp_y,component,
                fontsize=7,color=line_color,
                ha='center',va='center')

        # Add connecting line
        ax.plot([main_x + box_width,component_x],
                [y_pos,comp_y],
                color=line_color,linewidth=0.6,linestyle='-')

# Draw arrows between main steps
arrow_head_width = 0.15
arrow_head_length = 0.15
for i in range(len(steps) - 1) :
    ax.arrow(
        main_x + box_width / 2,y_positions[i] - box_height / 2 - 0.05,
        0,-spacing + box_height + 0.1,
        head_width=arrow_head_width,head_length=arrow_head_length,
        fc=line_color,ec=line_color,linewidth=1.2
    )

# Add feedback loop arrow (from bottom to top)
feedback_x = main_x - 1.2
ax.plot(
    [main_x,feedback_x,feedback_x,main_x],
    [y_positions[-1],y_positions[-1],y_positions[0],y_positions[0]],
    color="#e74c3c",linewidth=1.1,linestyle='-'
)
# Add arrowhead for feedback loop
ax.arrow(
    feedback_x,y_positions[0],
    0.5,0,
    head_width=arrow_head_width,head_length=arrow_head_length,
    fc="#e74c3c",ec="#e74c3c",linewidth=0
)
# Add feedback loop text
ax.text(
    feedback_x - 0.1,(y_positions[0] + y_positions[-1]) / 2,
    "Continuous\nImprovement\nFeedback\nLoop",
    fontsize=7,color="#e74c3c",ha='right',va='center',
    rotation=90
)

# Add title
plt.suptitle("AI and Machine Learning in Chatbot Functionality",
             fontsize=12,fontweight='bold',y=0.98)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.95)

plt.show()
import collections 
import collections.abc
from pptx import Presentation

def create_complaint_presentation():
    prs = Presentation()
    slide_layout = prs.slide_layouts[0] 
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Campus Complaint & Issue Tracker"
    subtitle.text = "A College Project Demonstration"

    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "The Problem"
    tf = content.text_frame
    tf.text = "Reporting campus issues (broken lights, lab issues) is disorganized."
    p = tf.add_paragraph()
    p.text = "- Paper forms get lost."
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Students have no way to track issue resolutions."
    p.level = 1

    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "The Solution"
    tf = content.text_frame
    tf.text = "A centralized ticketing platform."
    p = tf.add_paragraph()
    p.text = "- Student Portal: Submit issues with image evidence and track status."
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Admin Dashboard: Filter incoming complaints by category and resolve them."
    p.level = 1

    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "Technology Stack"
    tf = content.text_frame
    tf.text = "- Backend: Python & Django"
    p = tf.add_paragraph()
    p.text = "- Frontend: HTML, CSS, Bootstrap 5"
    p = tf.add_paragraph()
    p.text = "- Image Handling: Django Media & Pillow"
    p = tf.add_paragraph()
    p.text = "- Database: SQLite"

    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "Database Structure"
    tf = content.text_frame
    tf.text = "Relationships model the real world."
    p = tf.add_paragraph()
    p.text = "- Complaint relates to User via ForeignKey"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Support remarks logged directly onto Complaint instances"
    p.level = 1

    prs.save("Complaint_Tracker_Presentation.pptx")

create_complaint_presentation()

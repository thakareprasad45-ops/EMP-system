import collections 
import collections.abc
from pptx import Presentation

def create_attendance_presentation():
    prs = Presentation()
    slide_layout = prs.slide_layouts[0] 
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Student Attendance Management System"
    subtitle.text = "A College Project Demonstration"

    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "The Problem"
    tf = content.text_frame
    tf.text = "Tracking attendance manually is slow and error-prone."
    p = tf.add_paragraph()
    p.text = "- Teachers waste class time on roll calls."
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Students lack visibility into their attendance records."
    p.level = 1

    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "The Solution"
    tf = content.text_frame
    tf.text = "A centralized Django web platform."
    p = tf.add_paragraph()
    p.text = "- Teacher Dashboard: Create subjects, manage students, bulk mark attendance."
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Student Dashboard: View real-time attendance percentage."
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
    p.text = "- Database: SQLite"

    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "Key Django Concepts Used"
    tf = content.text_frame
    tf.text = "MVT Architecture (Model, View, Template)"
    p = tf.add_paragraph()
    p.text = "Django ORM for easy database queries"
    p = tf.add_paragraph()
    p.text = "ForeignKeys (e.g. Attendance relates to Student & Subject)"
    p = tf.add_paragraph()
    p.text = "Role-based Authentication (Teacher vs. Student)"

    prs.save("Attendance_System_Presentation.pptx")

create_attendance_presentation()

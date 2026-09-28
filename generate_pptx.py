import collections 
import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

def create_presentation():
    prs = Presentation()
    
    # Slide 1: Title Slide
    slide_layout = prs.slide_layouts[0] 
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "EMS PRO"
    subtitle.text = "Employment Management System\nA College Project Demonstration"

    # Slide 2: Problem Statement
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "The Problem"
    tf = content.text_frame
    tf.text = "Modern hiring is fragmented and chaotic."
    p = tf.add_paragraph()
    p.text = "- Job seekers struggle to track application statuses."
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Employers lose track of candidates across platforms."
    p.level = 1

    # Slide 3: Our Solution (EMS PRO)
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "The Solution: EMS PRO"
    tf = content.text_frame
    tf.text = "A centralized platform built with Django."
    p = tf.add_paragraph()
    p.text = "- Employee Portal: Browse, Apply, Track."
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Employer Portal: Post Jobs, Review Resumes, Change Status."
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Admin Dashboard: Total control over the platform."
    p.level = 1

    # Slide 4: Technology Stack
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "Technology Stack"
    tf = content.text_frame
    tf.text = "Built entirely with modern, reliable technologies."
    p = tf.add_paragraph()
    p.text = "- Backend: Python & Django"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Database: SQLite"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Frontend: HTML5 & Bootstrap 5"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Architecture: MVT (Model-View-Template)"
    p.level = 1

    # Slide 5: System Features
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "Key Features"
    tf = content.text_frame
    tf.text = "Secure Role-Based Authentication"
    p = tf.add_paragraph()
    p.text = "File Uploads (Resumes)"
    p = tf.add_paragraph()
    p.text = "Django ORM for Database Management"
    p = tf.add_paragraph()
    p.text = "Cross-Site Request Forgery (CSRF) Protection"

    # Slide 6: Database Relationships
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "Database Structure"
    tf = content.text_frame
    tf.text = "Robust relational modeling."
    p = tf.add_paragraph()
    p.text = "- User ↔ Profile (One-to-One)"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Company → Jobs (One-to-Many)"
    p.level = 1
    p = tf.add_paragraph()
    p.text = "- Job → Applications (One-to-Many)"
    p.level = 1

    # Slide 7: Live Demo
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = "Live Demonstration"
    tf = content.text_frame
    tf.text = "Let's see EMS PRO in action!"
    p = tf.add_paragraph()
    p.text = "1. Employee applies for a job."
    p.level = 1
    p = tf.add_paragraph()
    p.text = "2. Employer reviews application."
    p.level = 1
    
    # Save Presentation
    prs.save("EMS_PRO_Presentation.pptx")

if __name__ == "__main__":
    create_presentation()

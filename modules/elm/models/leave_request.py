from django.db import models

class LeaveRequest(models.Model):
    user_id = models.IntegerField()
    leave_type = models.ForeignKey("LeaveType", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ("draft", "Draft"),
        ("submitted", "Submitted"),
        ("under_review", "Under review"),
        ("shortlisted", "Shortlisted"),
        ("interview_scheduled", "Interview scheduled"),
        ("selected", "Selected"),
        ("rejected", "Rejected"),
        ("withdrawn", "Withdrawn"),
        ("auto_withdrawn", "Withdrawn automatically"),
        ("offer_issued", "Offer issued"),
        ("offer_accepted", "Offer accepted"),
        ("offer_declined", "Offer declined"),
        ("offer_expired", "Offer expired"),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"LeaveRequest {self.id} for user {self.user_id}"

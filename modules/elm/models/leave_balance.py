from django.db import models

class LeaveBalance(models.Model):
    user_id = models.IntegerField()
    leave_type = models.ForeignKey("LeaveType", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"LeaveBalance for user {self.user_id} and type {self.leave_type}"

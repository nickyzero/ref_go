from django import forms
from .models import *

'''
gid_errormessages={
    'required': '해당 항목은 필수 입니다!',
    'min_length': '최소 %(limit_value)d자 이상 입력해 주세요!',
}


class SettingUserForm(forms.ModelForm):
    class Meta:
        model = Setting_user
        fields = ('gid')
        gid = forms.CharField(label="gid", min_length=4, max_length=12, required=True,
                          error_messages= gid_errormessages)
     def save(self, user=None):
        setting_user = super(SettingUserForm, self).save(commit=False)
        if gid:
            user_profile.user = user
        user_profile.save()
        return user_profile

'''
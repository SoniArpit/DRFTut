from rest_framework.throttling import UserRateThrottle


class TonyUserRateThrottle(UserRateThrottle):
    scope = 'tony'

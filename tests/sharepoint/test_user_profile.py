from tests.sharepoint.sharepoint_case import SPTestCase

from office365.sharepoint.userprofiles.profileLoader import ProfileLoader


class TestUserProfile(SPTestCase):
    profile_loader = None  # type: ProfileLoader

    def test1_get_profile_loader(self):
        profile_loader = ProfileLoader.get_profile_loader(self.client).execute_query()
        self.__class__.profile_loader = profile_loader

    def test2_get_profile_loader(self):
        user_profile = self.__class__.profile_loader.get_user_profile().execute_query()
        self.assertIsNotNone(user_profile.properties["AccountName"])

    def test3_create_personal_site(self):
        user_profile = self.__class__.profile_loader.get_user_profile()
        user_profile.create_personal_site_enque(True).execute_query()

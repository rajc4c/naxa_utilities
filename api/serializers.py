import random
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MedicalFacility, MedicalFacilityCategory, \
    MedicalFacilityType, CovidCases, Province, ProvinceData, District, \
    Municipality, UserRole, UserLocation, UserReport, AgeGroupData, \
    DistrictData, MuniData, GlobalData, MobileVersion


class MedicalFacilityCategorySerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = MedicalFacilityCategory
        fields = ('id', 'name', 'type')

    def get_type(self, obj):
        qs = obj.Category.all().order_by('id').values('id', 'name')
        return qs


class MedicalFacilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalFacilityType
        fields = "__all__"


class MedicalFacilitySerializer(serializers.ModelSerializer):
    ownership_display = serializers.CharField(source="get_ownership_display",
                                           read_only=True)
    district_name = serializers.SerializerMethodField()
    province_name = serializers.SerializerMethodField()
    municipality_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    type_name = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()

    class Meta:
        model = MedicalFacility
        # fields = ('name', 'id', 'num_of_bed', 'contact_num', 'is_used_for_Corona_response', 'num_of_icu_ward',
        #           'num_of_ventilators', 'num_of_isolation_ward', 'remaining_capacity', 'remarks', 'lat',)
        fields = "__all__"

    def get_district_name(self, obj):
        if obj.district:
            return obj.district.name
        return ""

    def get_province_name(self, obj):
        if obj.province:
            return obj.province.name
        return ""

    def get_municipality_name(self, obj):
        if obj.municipality:
            return obj.municipality.name
        return ""

    def get_type_name(self, obj):
        if obj.type:
            return obj.type.name
        return ""

    def get_category_name(self, obj):
        if obj.category:
            return obj.category.name
        return ""

    def get_distance(self, obj):
        if hasattr(obj, "distance"):
            return obj.distance
        return 0


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidCases
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = "__all__"


class ProvinceDataSerializer(serializers.ModelSerializer):
    facility_count = serializers.SerializerMethodField()

    class Meta:
        model = ProvinceData
        fields = "__all__"

    def get_facility_count(self, obj):
        if hasattr(obj, "facility_count"):
            return obj.facility_count
        return MedicalFacility.objects.filter(province=obj.province_id).count()


class UserRoleSerializer(serializers.ModelSerializer):
    group_name = serializers.SerializerMethodField()
    facility_name = serializers.SerializerMethodField()
    province_name = serializers.SerializerMethodField()

    class Meta:
        model = UserRole
        fields = ("group", "province", "facility", "group_name",
                  "province_name", "facility_name")

    def get_group_name(self, obj):
        if obj.group:
            return obj.group.name
        return ""

    def get_province_name(self, obj):
        if obj.province:
            return obj.province.name
        return ""

    def get_facility_name(self, obj):
        if obj.facility:
            return obj.facility.name
        return ""


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = "__all__"


class UserReportSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    class Meta:
        model = UserReport
        fields = "__all__"

    def get_result(self, obj):
        if obj.has_travel_history or obj.has_convid_contact:
            return "morelikely"
        if obj.temperature >= 102 and obj.fast_breathe:
            return "likely"
        return "lesslikely"

    def validate(self, data):
        """
        Check that lat long present.
        """
        if not data['lat'] or not data['long']:
            data['lat'] = random.choice([27.61824026, 27.62824026,
                                                 27.63824026, 27.64824026])
            data['long'] = random.choice([85.46619027, 85.36619027,
                                                  85.26619027, 85.16619027,
                                                  85.56619027])
        return super(UserReportSerializer, self).validate(data)


class AgeGroupDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroupData
        fields = "__all__"


class SpaceSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = MedicalFacility
        exclude = ()

    def get_distance(self, obj):
        a = float(''.join([x for x in str(obj.distance) if x != 'm']).strip()) / 1000
        return str("{0:.3f}".format(a)) + 'km'


class DistrictDataSerializer(serializers.ModelSerializer):
    facility_count = serializers.SerializerMethodField()

    class Meta:
        model = DistrictData
        fields = "__all__"

    def get_facility_count(self, obj):
        if hasattr(obj, "facility_count"):
            return obj.facility_count
        return MedicalFacility.objects.filter(district=obj.district_id).count()


class MuncDataSerializer(serializers.ModelSerializer):
    facility_count = serializers.SerializerMethodField()

    class Meta:
        model = MuniData
        fields = "__all__"

    def get_facility_count(self, obj):
        if hasattr(obj, "facility_count"):
            return obj.facility_count
        return MedicalFacility.objects.filter(
            municipality=obj.municipality_id).count()


class GlobalDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlobalData
        fields = "__all__"


class MobileVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobileVersion
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

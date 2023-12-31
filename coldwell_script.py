# -*- coding: utf-8 -*-
"""Coldwell script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttzRpK5aRr-IAN7eqLl9p83-McIPS4Wq
"""

df = pd.read_excel(fr"{coldwell_sheet_path}")
projct_table = pd.read_excel(fr"{old_projets_sheet_path}")
export_at = coldwell_sheet_path.replace(coldwell_sheet_path.split("/")[-1], "") + "Coldwell Export"
if not os.path.exists(export_at):
    os.makedirs(export_at)
                              ### ======================= MAPS ======================= ###

translation = {'Twin': 'توين', 'Two Bedrooms Apartment': 'شقة مكونة من غرفتي نوم', 'Three Bedrooms Apartment': 'شقة مكونة من 3 غرف نوم', 'Four Bedrooms Apartment': 'شقة مكونة من 4 غرف نوم', 'Penthouse': 'بنتهاوس', 'Chalet': 'شاليه', 'Townhouse': 'تاون هاوس', 'Villa': 'فيلا', 'Apartment': 'شقة', 'Phase 9': 'المرحلة 9', 'Twin House': 'توين هاوس', 'Aquamarine': 'أكوا مارين', 'Onyx': 'أونيكس', 'Aqua': 'أكوا', 'Pearl': 'بيرل', 'Jade': 'Jade', 'Sapphire': 'Sapphire', 'Emerald': 'إميرالد', 'Amber': 'أمبر', 'Topaz': 'توباز', 'Opal': 'أوبال', 'Jasper': 'Jasper', 'Studio': 'استوديو', 'Cabin': 'كابينة', 'Ground Floor': 'طابق أرضي', 'Typical Floor': 'طابق نموذجية', 'One Bedroom Apartment': 'شقة مكونة من غرفة نوم واحدة', 'One bedroom Apartment.': 'شقة مكونة من غرفة نوم واحدة.', 'Duplex': 'دوبلكس', 'Phase 16': 'المرحلة 16', 'Phase X': 'المرحلة العاشرة', 'I Villa': 'أي فيلا', 'I-Villa': 'آي فيلا', 'Phase 3': 'المرحلة 3', 'Hotel Suits': 'أجنحة فندقية', 'Twin house': 'توين هاوس', 'Typical Floor - Terraces': 'طابق نموذجي - تراسات', 'Taj sultan 2 bedroom': 'شقة تاج سلطان مكونة من غرفتي نوم', 'Twin-house': 'توين هاوس', 'Garden Terraces': 'تراسات الحديقة', 'Penthoues': 'بنتهاوس', 'Lagoon View 2 Bedrooms + Private pool': 'شقق لاجون فيو مكونة من غرفتي نوم + حمام سباحة خاص', 'Zone C': 'المنطقة C', 'WV - Oak': 'WV - Oak', 'Phase 1': 'المرحلة 1', 'Ground Floor - Garden': 'طابق أرضي - حديقة', 'TownHouse': 'تاون هاوس', 'Patio- Twin Villa': 'الباتيو - فيلا توين هاوس', 'Lodges': 'كوخ  للاستجمام', 'Townhouse Middle': 'تاون هاوس ميدل', 'Townhouse Corner': 'تاون هاوس كورنر', 'Ground Villa': 'فيلا أرضية', 'Middle Annex': 'Middle Annex', 'Appartment': 'شقة', 'Phia ( 2BR )': 'Phia (2 غرف نوم)', 'ELARA': 'إلارا ELARA ', 'Town House': 'تاون هاوس', 'Sky Villa': 'فيلا سكاي', 'S Villa': 'S فيلا ', 'Twinhouse': 'توين هاوس', 'Twin-House': 'توين هاوس', 'villa': 'فيلا', 'one Bedroom Apartment.': 'شقة بغرفة نوم واحدة.', 'Standalone Villas': 'فيلات مستقلة', 'Two bedrooms Apartment.': 'شقة مكونة من غرفتي نوم.', 'Three bedrooms Apartment.': 'شقة مكونة من 3 غرف نوم.', 'studio': 'استوديو', 'Four bedrooms Apartment.': 'شقة مكونة من أربع غرف نوم.', 'Apartment + Garden': 'شقة + حديقة', 'Apartment + Roof': 'شقة + روف', 'Only Ground': 'طابق أرضي فقط', 'Water Villa': 'ووتر فيلا', 'Phase 4': 'المرحلة 4', 'apartment': 'شقة', 'penthouse': 'بنتهاوس', 'Attached Villa': 'فيلا ملحقة', 'Maesta': 'Maesta', 'Chalets': 'شاليهات', 'Town house': 'تاون هاوس', 'Standard Ground Floor': 'طابق أرضي قياسي ', '1 Bedroom': 'غرفة نوم واحدة', 'Small': 'صغير', '2 Allocated Parking Spots': '2 أماكن مخصصة لانتظار السيارات', 'Retail': 'مساحات للبيع بالتجزئة', 'Clinic': 'عيادة', 'Offices': 'مكاتب', 'duplex': 'دوبلكس', 'Privida': 'Privida', 'Clinics': 'عيادات', 'Phase 2': 'المرحلة 2', 'Chalat': 'شاليهات', 'cabin': 'كابينة', 'Apartments': 'شقق', 'Garden View Villa': 'جاردن فيو فيلا', 'Sea Front Villa': 'فيلا مواجهة للبحر', 'Standalone villa': 'فيلا مستقلة', 'Family House': 'فاميلي هاوس', 'Office Space': 'مساحة مكتبية', 'Stand Alone': 'مستقلة', 'Duo': 'مزدوج', 'Twin Chalet': 'توين شاليه ', 'The Gate': 'البوابة', 'The Park': 'الحديقة', 'Standalone': 'مستقلة', 'Clinc': 'عيادة', '1 Bedroom apartment': 'شقة مكونة من غرفة نوم واحدة', '2 Bedroom apartment': 'شقة مكونة من غرفتي نوم', '1-Bedroom': 'غرفة نوم واحدة', '2-Bedroom': 'غرفتي نوم', '3-Bedroom': '3 غرف نوم', 'Garden Terrace': 'تراس الحديقة', 'Office Spaces': 'مساحات مكتبية', 'Duplex Ground': 'دوبلكس طابق أرضي ', 'Duplex Roof': 'روف دوبلكس', 'Park Villa': 'بارك فيلا ', 'Townhomes': 'وحدات تاون هوم', 'Villas': 'فيلات', 'Terrace (51-58)': 'تراس (51-58)', 'Roof Terrace (89-96)': 'تراس بالروف (89-96)', 'Twinvilla': 'فيلا توين هاوس', 'Apartment Type A': 'شقة Type A', 'Apartment Type B': 'شقة Type B', 'Apartment Type C': 'شقة Type C', 'Town houses': 'وحدات تاون هاوس', 'Twin Houses': 'وحدات توين هاوس', 'Cielo Villa': 'Cielo Villa', 'Clinics & Admin': 'العيادات والمباني الإدارية', 'Admin': 'مبنى إداري', '2 bedrooms': 'غرفتي نوم', '3 bedrooms': '3 غرف نوم', '3 Bedrooms': '3 غرف نوم', '2 Bedroom': 'غرفتي نوم', '3 Bedroom': '3 غرف نوم', 'Terrace (7-21)': 'تراس (7-21)', 'Terrace (6-12)': 'تراس (6-12)', 'Terrace (9-16)': 'تراس (9-16)', 'Terrace (23-39)': 'تراس (23-39)', 'Terrace (102.58)': 'تراس (102.58)', 'Terrace (10.36)': 'تراس (10.36)', '2 Bedrooms': 'غرفتي نوم', 'Standard 1st floor': 'الطابق الأول القياسي', 'Standard 2nd floor': 'الطابق الثاني القياسي', 'Prime Ground Floor': 'الطابق الأرضي الرئيسي', 'Prime 1st Floor + Pent House': 'الطابق الأرضي الرئيسي + بنتهاوس', 'Medium': 'متوسط', 'Large': 'كبير', 'Sea View 2 Bedrooms': 'فيلا مكونة من غرفتي نوم مطلة على البحر', 'Sea View 3 Bedrooms': 'فيلا مكونة من 3 غرف نوم مطلة على البحر', 'Lagoon View 3 Bedrooms': 'لاجون فيو فيلا مكونة من 3 غرف نوم', 'Medical Centre': 'مركز طبي', 'Hospital': 'مستشفى', 'residential Towers': 'أبراج سكنية', 'Grand Villa': 'فيلا كبيرة (جراند فيلا)', 'Twin Villa': 'فيلا توين هاوس', 'B': 'B', 'A': 'A', 'C': 'C', 'Corner': 'كورنر', 'Graded': 'متدرج', 'Middle': 'ميدل', '2 Bedrooms typical floor': 'شقة مكونة من غرفتي نوم في طابق متكرر', '2 Bedrooms ground floor + garden': 'شقة مكونة من غرفتي نوم في الطابق الأرضي + حديقة', '3 Bedrooms apartment with garden': 'شقة مكونة من 3 غرف نوم مع حديقة', '3 Bedrooms typical apartment': 'شقة نموذجية مكونة من 3 غرف نوم', 'Small penthouse 3 bedrooms + 160 m open roof': 'بنتهاوس صغير مكون من 3 غرف نوم + روف مفتوح بمساحة 160 متر ', 'Large penthouse 4 bedrooms + 102 m roof': 'بنتهاوس كبير مكون من 4 غرف نوم + روف بمساحة 102 متر ', 'Medium penthouse 4 bedrooms + 106 m roof': 'بنتهاوس متوسط مكون من 4 غرف نوم + روف بمساحة 106 م', 'Senior': 'Senior', 'Pool Deck': 'حمام سباحة', 'One bed room': 'غرفة نوم واحدة', 'Two bed rooms': 'غرفتي نوم', 'Three bed rooms': '3 غرف نوم', 'First Floor': 'الطابق الأول', 'Garden Apartments': 'شقق بحدائق', 'View ( Inner Road ) & Garden': 'إطلالة على (الطريق الداخلي) وحديقة', 'Small Villa': 'فيلا صغيرة', 'Medium Villa': 'فيلا متوسطة', 'Aura': 'أورا', 'Oriana IV': 'Oriana IV', 'Twin houses': 'وحدات توين هاوس', '4 Bedrooms': '4 غرف نوم', 'Villa A': 'فيلا A', 'Villa B': 'فيلا B', 'Villa C': 'فيلا ج', 'Villa D': 'فيلا D', 'Town house Corner': 'تاون هاوس كورنر', 'Town House Middle': 'تاون هاوس ميدل', 'Bo1: 3 bedrooms': 'رقم 1: 3 غرف نوم', 'Bo1: 2 bedrooms': 'رقم 1: غرفتي نوم', 'Bo1: 1 bedroom': 'رقم 1: غرفة نوم واحدة', 'Bo2: 3 bedrooms': 'رقم 2: 3 غرف نوم', 'Bo2: 2 bedrooms': 'رقم 2: غرفتي نوم', 'Bo3L: 3 bedrooms': 'Bo3L: 3 غرف نوم', 'Bo3L: 2 bedrooms': 'Bo3L: غرفتي نوم', 'Bo3s: 3 bedrooms': 'Bo3s: 3 غرف نوم', 'Bo3s: 2 bedrooms': 'Bo3s: غرفتي نوم', 'Bo4: 3 bedrooms': 'رقم 4: 3 غرف نوم', 'Bo4: 1 bedroom': 'رقم 4: غرفة نوم واحدة', 'Standalone Villa Type A': 'فيلا مستقلة Type A', 'Standalone Villa Type B': 'فيلا مستقلة Type B', 'Standalone Villa Type C': 'فيلا مستقلة Type C', 'Standalone Villa Type C2': 'فيلا مستقلة Type C2', 'Type D2': 'Type D2', 'Type D': 'Type D', 'Type F': 'Type F', '3 bedroom': '3 غرف نوم', 'Underground Parking': 'أماكن انتظار سيارات تحت الأرض', 'Stand Alone ( Meduim Villa)': 'فيلا مستقلة (فيلا متوسطة)', 'Avenus': 'Avenus', 'Phase 5': 'المرحلة 5', 'Studios': 'شقق استوديو', 'Garden (55-155)': 'حديقة (55-155)', 'Terrace (20-45)': 'تراس (20-45)', 'Terrace (19-33)': 'تراس (19-33)', 'Terrace (7.7-8.5)': 'تراس (7.7-8.5)', 'Terrace (7.5-9.5)': 'تراس (7.5-9.5)', 'Retails': 'Retails', 'Type C': 'Type C', 'Twin Terraces': 'تراس مزدوج', 'Zone V': 'المنطقة  V', 'Zone E': 'المنطقة E', 'I villas': 'وحدات آي فيلا ', 'Town House Corner': 'تاون هاوس كورنر', 'Townhouses': 'وحدات تاون هاوس', 'Twin Corner': 'توين كورنر', '1 Bedroom Standard': 'غرفة نوم موحدة', '3 Bedroom Central': '3 غرف نوم سنترال', '3 Bedroom Penthouse': 'بنتهاوس مكون من 3 غرف نوم', '4 Bedroom Penthouse 226': 'بنتهاوس مكون من 4 غرف نوم 226', 'Town Houses': 'وحدات تاون هاوس', 'Chalets 3 Bed Ground Floor': 'شاليهات 3 غرف نوم طابق أرضي', '2 Bedrooms -1st Floor': 'غرفتي نوم - الطابق الأول', '2 Bedrooms - 2nd Floor': 'غرفتي نوم - الطابق الثاني', '2 Bedrooms - Ground Floor': 'غرفتي نوم - الطابق الأرضي', '3 Bedrooms - 1st Floor': '3 غرف نوم - الطابق الأول', '3 Bedrooms - 2nd floor': '3 غرف نوم - الطابق الثاني', '3 Bedrooms - Ground floor': '3 غرف نوم - الطابق الأرضي', 'Standalone Lagoon': 'لاجون مستقلة', 'Middle 3 Bedrooms': '3 غرف نوم ميدل', 'Corner 3 or 4 Bedrooms': 'كورنر مكون من 3 أو 4 غرف نوم', 'Front 3 or 4 Bedrooms': 'وحدات أمامية مكون من 3 أو 4 غرف نوم', 'HQ50': 'مرحلة HQ50', 'One Bedroom': 'غرفة نوم واحدة', 'Two Bedrooms': 'غرفتي نوم', 'Two Bedroom with roof': 'غرفتي نوم مع روف', 'Three Bedrooms': 'ثلاث غرف نوم', 'Apartments 1 bed room': 'شقق مكونة من غرفة نوم واحدة', 'Apartments 2 bed room': 'شقق مكونة من غرفتي نوم', 'Apartments 3 bed room': 'شقق مكونة من 3 غرف نوم', 'Mazarine': 'مزارين', 'Loft': 'لوفت', 'Typical Floor- Main Terraces': 'طابق نموذجي - تراسات رئيسية', 'Serviced Apartment': 'شقة مزودة بخدمات فندقية', '1 Allocated Parking Spot': 'منطقة مخصصة لانتظار السيارات', 'Lake Yard Chalets': 'شاليهات بكمبوند ليك يارد', 'Golf View Chalet': 'شاليه بكمبوند جولف فيو', 'Sky Loft " Millenial1"': 'سكاي لوفت «ميلينيال1"', 'Millenial apartment "Millenial1"': 'شقة ميلينيال «ميلينيال 1"', 'Garden " Millenial 1"': 'حديقة «ميلينيال 1"', 'Sky Loft " Millenial 3"': 'سكاي لوفت «ميلينيال 3"', 'Millenial apartment "Millenial 3"': 'شقة ميلينيال «ميلينيال 3"', 'Garden " Millenial 3"': 'حديقة «ميلينيال 3"', 'Ivilla Roof': 'روف آي فيلا ', 'Sky Garden': 'سكاي جاردن', 'Ivilla Garden': 'حديقة آي فيلا ', 'One Story House': 'منزل مكون من طابق واحد', 'Lake House': 'ليك هاوس ', 'Phase 17': 'المرحلة 17', '1 Bedroom park towers': 'بارك تاورز - غرفة نوم واحدة', '2 Bedrooms park towers': 'بارك تاورز - غرفتي نوم', '3 Bedroom park towers': 'بارك تاورز -  3 غرف نوم ', '4 Bedroom Park towers': 'بارك تاورز -4 غرف نوم', 'Premium Chalet': 'شاليه بريميوم', 'Middle Townhouse': 'تاون هاوس ميدل', 'Corner Townhouse': 'تاون هاوس كورنر ', 'Taj sultan 3 bedroom': 'وحدات تاج سلطان مكونة من 3 غرف نوم', 'Shalya 1 bedroom': 'وحدات شاليا مكونة من غرفة نوم', 'Shayla 2 Bedroom': 'وحدات شاليا مكونة من غرفتي نوم', 'Shalya 3 bedroom': 'وحدات شاليا مكونة من 3 غرف نوم', 'Lake park 2 Bedroom': 'وحدات ليك بارك مكونة من غرفتي نوم', 'Lake park 3 Bedroom': 'وحدات ليك بارك مكونة من 3 غرف نوم', 'Taj Gardens 1 Bedroom': 'وحدات تاج جاردنز مكونة من غرفة نوم', 'Taj Gardens 2 Bedroom': 'وحدات تاج جاردنز مكونة من غرفتي نوم', 'Taj Gardens 3 Bedroom': 'وحدات تاج جاردنز مكونة من 3 غرف نوم', 'Stand alone': 'مستقلة', 'Office spaces': 'مساحات مكتبية', 'Retail spaces': 'مساحات Retail ', 'F&B spaces': 'مساحات لبيع المأكولات والمشروبات', '1 Bedroom With Roof': 'وحدة مكونة من غرفة نوم واحدة مع روف', '2 Bedroom With Roof': 'وحدة مكونة من غرفتي نوم مع روف', 'Studio With Roof': 'شقة استوديو مع روف', 'Pharmacy': 'صيدلية', 'HQ500': ' مرحلة HQ500', 'HQ500i': ' مرحلة HQ500i', 'Administrative offices': 'مكاتب إدارية', 'Administrative': 'إداري', 'Drive Beach': 'درايف بيتش Drive Beach', 'Lagoon Beach': 'لاجون بيتش', 'Brooks Villa A': 'فيلا (أ) بكمبوند ذا بروكس', 'Brooks Villa B': 'فيلا (ب) بكمبوند ذا بروكس', 'Pent House': 'بنتهاوس', 'Phase 2- Zone T': 'المرحلة 2 - المنطقة T', 'Phase 2- Zone T CS': 'المرحلة 2 - المنطقة T CS', 'Phase 2- Zone E': 'المرحلة 2 - المنطقة E', 'Zone A': 'المنطقة A', 'Zone CS': 'المنطقة CS', 'Terrace (74.5)': 'تراس (74.5)', 'Phase 2-3': 'المرحلة 2-3', 'Pent Cloud ,7th floor': 'Pent Cloud، الطابق السابع', 'Garden (106)': 'حديقة (106)', 'Garden - Terraces': 'حديقة - تراسات', 'Middle - Terraces - Garden': 'ميدل - تراسات - حديقة', 'Corner - Terraces - Garden': 'كورنر - تراسات - حديقة', 'Standalone Type A': 'فيلا مستقلة Type A', 'Standalone Type B': 'فيلا مستقلة Type B', 'Standalone Type C': 'فيلا مستقلة Type C', 'Cozy Loft': 'لوفت مريح', 'Junior Loft': 'لوفت صغير', 'Panoramic Loft': 'لوفت بانورامي', 'Senior Loft': 'لوفت سينيور ', 'Festival Living': 'فيستيفال ليفينج', 'Ground Duplex': 'دوبلكس أرضي', 'Typical Duplex': 'دوبلكس نموذجي', 'The Boulevard': 'ذا بوليفارد', 'The Corner': 'ذا كورنر', 'Trio': 'ثلاثي', 'Garden (73-106)': 'حديقة (73-106)', 'Terrace (0-40)': 'تراس (0-40)', 'Quadro Villa': 'فيلا كوادرو', 'Garden (174-182)': 'حديقة (174-182)', 'Roof Terrace (0-8)': 'تراس بالروف (0-8)', 'Terraces Apartment': 'شقة Terraces ', 'Zone B': 'المنطقة B', 'Terrace (11-21)': 'تراس (11-21)', 'Creek Villas': 'فيلات كريك Creek Villas', 'Terrace (24-48)': 'تراس (24-48)', 'Terrace (8-12)': 'تراس (8-12)', 'Terrace (15-16)': 'تراس (15-16)', 'Terrace (32.6)': 'تراس (32.6)', 'Terrace (7-12)': 'تراس (7-12)', 'Terrace (16.6)': 'تراس (16.6)', 'Cliff Villas': 'فيلات كليف Cliff Villas', 'Garden Villa': 'فيلا جاردن', 'Double View House': 'منزل Double View', 'Sky Villas': 'فيلات سكاي', 'Phase VIII': 'المرحلة الثامنة', 'Phase I': 'المرحلة الأولى', 'Phase IV': 'المرحلة الرابعة', 'Phase XIV': 'المرحلة الرابعة عشرة', 'Phase III': 'المرحلة الثالثة', 'Zone 2': 'المنطقة 2', 'Zone 3': 'المنطقة 3', 'Old Zones': 'المناطق القديمة', 'WV - Pine': 'WV - Pine', 'WV - Pine 1': 'WV - Pine 1', 'Junior Chalet': 'جونيور شاليه ', 'Corner Loft': 'كورنر لوفت', 'Front Annex': 'ملحق أمامي', 'Middle Villa': 'فيلا ميدل', 'Phase 11': 'المرحلة 11', 'Phase 13': 'المرحلة 13', 'Mall': 'مجمع تجاري\n', 'Service Station': 'محطه خدمة', 'land': 'قطعة ارض', 'room': 'غرفة', 'Factory': 'مصنع', 'Store': 'متجر', 'Shop': 'متجر', "Commercial Project": 'مشروع تجاري', "Bank": "بنك", "Building": "مبنى", "Restaurant": "مطعم", "Medical": "طبي", "Food & Beverages": "الأطعمة والمشروبات", "Typical Chalet": "شاليه نموذجي", "Standalone Villa": "فيلا مستقلة", "Ground Chalet": "شاليه أرضي", "Senior Chalet": "شاليه سينيور", "Condo": "كوندو", "One Story Villa": "فيلا من طابق واحد" }
category_map = {'medical': 'Medical', 'pharmacy': 'Pharmacy', 'bank': 'Bank', 'food&beverages': 'Food & Beverages', 'cabanas': 'Cabanas', 'administrative': 'Administrative', 'loft': 'Loft', 'skyloft': 'Loft', 'condo': 'Sky Condos', 'commercialproject': 'Commercial Project', 'clinic': 'Clinic', 'medicaloffices': 'Clinic', 'clinics': 'Clinic', 'nursery': 'Nursery', 'shop': 'Shop', 'store': 'Store', 'mall': 'Mall', 'medicalcentre': 'Clinic Center', 'officespace': 'Office Space', 'retail': 'Retail', 'cabin': 'Cabin', 'elderhome': 'Building', 'building': 'Building', 'i-villa': 'I-Villa', 'twin-house': 'Twin-house', 'twinhouse': 'Twin-house', 'hotelsuits': 'Hotel', 'palace': 'Palace', 'standalone': 'Stand Alone', 'middletownhouse': 'Townhouse', 'cornertownhouse': 'Townhouse', 'townhouse': 'Townhouse', 'townhousemiddle': 'Townhouse', 'townhousecorner': 'Townhouse', 'standalonevilla': 'Villa', 'villa': 'Villa', 'skyvilla': 'Villa', 'quadrovilla': 'Villa', 'attachedvilla': 'Villa', 'onestoryvilla': 'Villa', 'gardenvilla': 'Villa', 'bridgevilla': 'Villa', 'springvilla': 'Villa', 'parkvilla': 'Villa', 'seafrontvilla': 'Villa', 'duplex': 'Duplex', 'typicalchalet': 'Chalet', 'groundchalet': 'Chalet', 'chalet': 'Chalet', 'premiumchalet': 'Chalet', 'juniorchalet': 'Chalet', 'chalets3bedgroundfloor': 'Chalet', 'twinchalet': 'Chalet', 'penthouse': 'Penthouse', 'apartment': 'Apartment', 'typicalapartment': 'Apartment', 'groundapartment': 'Apartment', 'hotelapartment': 'Apartment', 'servicedapartment': 'Apartment', 'terracesapartment': 'Apartment', 'studio': 'Studio', 'restaurant': 'Commercial Projet', "seniorchalet": "Chalet" }
finishing_map = {"Core & Shell": "تشطيب كور آند شل", "Finished":"تشطيب كامل", "Semi Finished": "تشطيب نصف كامل", "Flexi Finishing": "تشطيب مرن"}
Deliver_Status_map = {"onhold": "On Hold", "earlydelivery": "Early Delivery", "offplan": "Off Plan", "readytomove": "Ready to Move", "soldout": "Sold Out" }
comparing_new_and_old_projects = {}


                          ### ======================= Output Lists ======================= ###

Name,Starting_Price,Concept_Name,Area_From,Area_To,Finishing,Description,Is_Sold,Price_Per_Meter,Category,Project,Status,Import_Type,Name_AR,Description_AR,Finishing_AR,show_in_price_indicator,ucn_has_error,error = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
Projects_list, Deliver_Statuses, Delivery_Dates, Down_Payment_list, Starting_Price_list, Installments_Years_list, Status_list = [], [], [], [], [], [], []


                      ### ======================= Projects_Units_Sheet ======================= ###

for ucn in df["Unit Concept Name"].unique():

    error_note = ""

    # ----------- Name, Project, Starting_Price, Concept_Name, Finishing, Status, Import_Type ----------- #
    Name.append(list(df[df["Unit Concept Name"] == ucn]["Unit Type"])[0])
    Project.append(list(df[df["Unit Concept Name"] == ucn]["Project Name  ↑"])[0] + " | " + list(df[df["Unit Concept Name"] == ucn]["Phase Name  ↑"])[0])
    Starting_Price.append(list(df[df["Unit Concept Name"] == ucn]["Price From"])[0])
    Concept_Name.append(ucn)
    Finishing.append(list(df[df["Unit Concept Name"] == ucn]["Finishing Type"])[0])
    Status.append("Published")
    Import_Type.append("units")


    # ----------- Area_From ----------- #
    #check if the area has decimals or not
    if int(list(df[df["Unit Concept Name"] == ucn]["Build Up Area From"])[0]) == list(df[df["Unit Concept Name"] == ucn]["Build Up Area From"])[0]:
        Area_From.append(int(list(df[df["Unit Concept Name"] == ucn]["Build Up Area From"])[0]))
    else:
        Area_From.append(list(df[df["Unit Concept Name"] == ucn]["Build Up Area From"])[0])


    # ----------- Area_To ----------- #
    #check if the area has decimals or not
    try:
        if int(list(df[df["Unit Concept Name"] == ucn]["Build Up Area To"])[0]) == list(df[df["Unit Concept Name"] == ucn]["Build Up Area To"])[0]:
            Area_To.append(int(list(df[df["Unit Concept Name"] == ucn]["Build Up Area To"])[0]))
        else:
            Area_To.append(list(df[df["Unit Concept Name"] == ucn]["Build Up Area To"])[0])
    except:
        Area_To.append(list(df[df["Unit Concept Name"] == ucn]["Build Up Area To"])[0])


    # ----------- Category ----------- #
    try:
      Category.append(category_map[str(list(df[df["Unit Concept Name"] == ucn]["Unit Type"])[0]).lower().replace(" ","")])
    except:
      print(ucn, f":{list(df[df['Unit Concept Name'] == ucn]['Unit Type'])[0]} Category not found")
      ucn_has_error.append(ucn)
      error_note += f" |{list(df[df['Unit Concept Name'] == ucn]['Unit Type'])[0]} Category not found"
      Category.append(np.nan)


    # ----------- Finishing_AR ----------- #
    try:
      Finishing_AR.append(finishing_map[list(df[df["Unit Concept Name"] == ucn]["Finishing Type"])[0]])
    except:
      print(ucn, f":{list(df[df['Unit Concept Name'] == ucn]['Finishing Type'])[0]} Finishing transation not found")
      ucn_has_error.append(ucn)
      error_note += f" |{list(df[df['Unit Concept Name'] == ucn]['Finishing Type'])[0]} Finishing transation not found"
      Finishing_AR.append(np.nan)


    # ----------- Name_AR ----------- #
    try:
      Name_AR.append(translation[list(df[df["Unit Concept Name"] == ucn]["Unit Type"])[0]])
    except:
      print(ucn, f":{list(df[df['Unit Concept Name'] == ucn]['Unit Type'])[0]} Name transation not found")
      ucn_has_error.append(ucn)
      error_note += f" |{list(df[df['Unit Concept Name'] == ucn]['Unit Type'])[0]} Name transation not found"
      Name_AR.append(np.nan)

    # ----------- Append ----------- #
    error.append(error_note)
    Description.append(np.nan)
    Is_Sold.append(0)
    Price_Per_Meter.append(0)
    Description_AR.append(np.nan)
    show_in_price_indicator = 1



                          ### ======================= Starting_price_Sheet ======================= ###

for project_name in df["Project Name  ↑"].unique():
    for phase in df[df["Project Name  ↑"] == project_name]["Phase Name  ↑"].unique():
        Projects_list.append(project_name+ " | "+ phase)
        Deliver_Statuses.append(Deliver_Status_map[re.sub(r'[^a-zA-Z0-9]', '', list(df[((df["Project Name  ↑"] == project_name) & (df["Phase Name  ↑"] == phase))]["Delivery Status"])[0].lower().replace(" ",""))])
        Delivery_Dates.append(f'1/1/{list(df[((df["Project Name  ↑"] == project_name) & (df["Phase Name  ↑"] == phase))]["Delivery Date"])[0]}')
        Down_Payment_list.append(min(list(df[((df["Project Name  ↑"] == project_name) & (df["Phase Name  ↑"] == phase))]["Down Payment"])))
        Starting_Price_list.append(min(list(df[((df["Project Name  ↑"] == project_name) & (df["Phase Name  ↑"] == phase))]["Price From"])))
        Installments_Years_list.append(max(list(df[((df["Project Name  ↑"] == project_name) & (df["Phase Name  ↑"] == phase))]["Years of Installments"])))
        Status_list.append("published")


                            ### ======================= Down_payments_Sheet ======================= ###

Down_payments = df[['Unit Concept Name', 'Down Payment', 'Years of Installments']].copy()
Down_payments = Down_payments.rename(columns = {'Unit Concept Name':'Concept Name', 'Down Payment': 'Downpayment', 'Years of Installments': 'Installments year'})
Down_payments.insert(2,"Sec Downpayment",np.nan)
Down_payments["Status"] = "published"



                          ### ======================= Ceating data frames ======================= ###

output_df = pd.DataFrame({"Name": Name,"Starting Price": Starting_Price,"Concept Name": Concept_Name, "Area From": Area_From, "Area To": Area_To, "Finishing":Finishing ,"Description": Description,"Is Sold": Is_Sold, "Price Per Meter": Price_Per_Meter,"Category": Category,"Project": Project, "Status": Status,"Import Type": Import_Type ,"Name AR": Name_AR, "Description AR": Description_AR,"Finishing AR": Finishing_AR, "Show in price indicator": show_in_price_indicator})
has_errors_df = pd.DataFrame({"Name": Name,"Starting Price": Starting_Price,"Concept Name": Concept_Name, "Area From": Area_From, "Area To": Area_To, "Finishing":Finishing ,"Description": Description,"Is Sold": Is_Sold, "Price Per Meter": Price_Per_Meter,"Category": Category,"Project": Project, "Status": Status,"Import Type": Import_Type ,"Name AR": Name_AR, "Description AR": Description_AR,"Finishing AR": Finishing_AR, "Error\s": error})
starting_price_df = pd.DataFrame({"Project": Projects_list, "Delivery Status": Deliver_Statuses,"Delivery Date": Delivery_Dates, "Down Payment": Down_Payment_list, "Starting Price": Starting_Price_list, "Installments Years":Installments_Years_list ,"Status": Status_list})

total = output_df.shape[0]  #<==== to check if the exported sheets are not missing any data


                ### ======================= Comparing New projects With old Projects ======================= ###

for index, row in projct_table.iterrows():
    comparing_new_and_old_projects[re.sub(r'[^a-zA-Z0-9]', '', str(row['Name']).lower().replace(" ",""))] = row['Name']

output_df['Project'] = output_df['Project'].apply(lambda x: comparing_new_and_old_projects[re.sub(r'[^a-zA-Z0-9]', '', str(x).lower().replace(" ",""))] if re.sub(r'[^a-zA-Z0-9]', '', str(x).lower().replace(" ","")) in comparing_new_and_old_projects else x)
starting_price_df['Project'] = starting_price_df['Project'].apply(lambda x: comparing_new_and_old_projects[re.sub(r'[^a-zA-Z0-9]', '', str(x).lower().replace(" ",""))] if re.sub(r'[^a-zA-Z0-9]', '', str(x).lower().replace(" ","")) in comparing_new_and_old_projects else x)


                    ### ======================= Fltring and splitting data frames ======================= ###

# ----------- Check if the ucn has an error or not  ----------- #
has_errors_df = has_errors_df[has_errors_df["Concept Name"].isin(ucn_has_error) == True]
output_df = output_df[output_df["Concept Name"].isin(ucn_has_error) == False]


# ----------- Check if the projet is already on the system or not  ----------- #
needs_to_be_added = output_df[~output_df.Project.isin(projct_table["Name"])]
output_df = output_df[output_df.Project.isin(projct_table["Name"])]


# ----------- Split down payment sheet depending on if the project is already on the system or not  ----------- #
Down_payments_to_upload = Down_payments[Down_payments["Concept Name"].isin(output_df["Concept Name"]) == True]
Down_payments_to_be_added = Down_payments[Down_payments["Concept Name"].isin(output_df["Concept Name"]) == False]


# ----------- Split starting price sheet depending on if the project is already on the system or not  ----------- #
starting_price_df_to_upload = starting_price_df[starting_price_df.Project.isin(projct_table["Name"])]
starting_price_df_to_be_added = starting_price_df[~starting_price_df.Project.isin(projct_table["Name"])]


                    ### ======================= Exporting Excel sheets ======================= ###

# Remove headers format from excel sheet
output_df.to_excel(r"{}\{}".format(export_at,"Coldwell ready_to_upload (units).xlsx"), index=False)
pd.io.formats.excel.ExcelFormatter.header_style = None  #<====== remove headers format from excel sheet


# ----------- ready_to_upload | needs_to_be_added | has_errors  ----------- #
output_df.to_excel(r"{}\{}".format(export_at,"Coldwell ready_to_upload (units).xlsx"), index=False)
has_errors_df.to_excel(r"{}\{}".format(export_at,"Coldwell has_errors.xlsx"), index=False)
needs_to_be_added.to_excel(r"{}\{}".format(export_at,"Coldwell needs_to_be_added (units).xlsx"), index=False)


# ----------- Down Payments|Starting Price + Add percentage format to the "Downpayment" columns  ----------- #

df_to_sheet = {"Down_payments_to_upload": [Down_payments_to_upload, "Coldwell ready_to_upload (Down Payments).xlsx", "B"],
      "Down_payments_to_be_added": [Down_payments_to_be_added, "Coldwell needs_to_be_added (Down Payments).xlsx", "B"],
      "starting_price_df_to_upload": [starting_price_df_to_upload, "Coldwell ready_to_upload (Starting Prices).xlsx", "D"],
    "starting_price_df_to_be_added": [starting_price_df_to_be_added, "Coldwell needs_to_be_added (Starting Prices).xlsx", "D" ]}

for key, value in df_to_sheet.items():
    excel_path = export_at + "\\" + value[1]

    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        value[0].to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        percentage_format = workbook.add_format({'num_format': '0%'})
        worksheet.set_column(f'{value[2]}:{value[2]}', None, percentage_format)


total == needs_to_be_added.shape[0] + has_errors_df.shape[0] + output_df.shape[0]
import pandas as pd
from business_rules.variables import BaseVariables

# Load data from CSV
data = pd.read_csv('C:/Users/Admin/Desktop/gen/GENPOP_SimData.csv')
class AF1Calculator(BaseVariables):
    def __init__(self, age, gender, af1):
        self.age = age
        self.gender = gender
        self.af1 = af1

    def calculate_af1_c(self):
        age_ranges = {
            'Male': {
                range(18, 26): {'Above Average': 100, 'Average': 90, 'Below Average': 80},
                range(26, 36): {'Above Average': 110, 'Average': 98.5, 'Below Average': 86},
                range(36, 46): {'Above Average': 115, 'Average': 101.5, 'Below Average': 89},
                range(46, 56): {'Above Average': 121, 'Average': 107.5, 'Below Average': 95},
                range(56, 66): {'Above Average': 128, 'Average': 112.5, 'Below Average': 98},
                range(66, 150): {'Above Average': 126, 'Average': 113, 'Below Average': 101}
            },
            'Female': {
                range(18, 26): {'Above Average': 104, 'Average': 94.5, 'Below Average': 86},
                range(26, 36): {'Above Average': 110, 'Average': 101, 'Below Average': 93},
                range(36, 46): {'Above Average': 115, 'Average': 105.5, 'Below Average': 97},
                range(46, 56): {'Above Average': 120, 'Average': 110.5, 'Below Average': 102},
                range(56, 66): {'Above Average': 129, 'Average': 117, 'Below Average': 106},
                range(66, 150): {'Above Average': 126, 'Average': 113.5, 'Below Average': 102}
            }
        }

        for age_range, categories in age_ranges[self.gender].items():
            if self.age in age_range:
                if self.af1 >= categories['Above Average']:
                    return 'Above Average'
                elif categories['Below Average'] <= self.af1 < categories['Above Average']:
                    return 'Average'
                else:
                    return 'Below Average'

        return 'Unknown'

def calculate_af1_c(row):
    af1_calculator = AF1Calculator(row['Age'], row['Gender'], row['AF1'])
    return af1_calculator.calculate_af1_c()


class AF2Calculator(BaseVariables):
    def __init__(self, age, gender, af2):
        self.age = age
        self.gender = gender
        self.af2 = af2

    def calculate_af2_c(self):
        age_ranges = {
            'Male': {
                range(20, 30): {'Above Average': 2700, 'Average': (1601, 2700), 'Below Average': 1600},
                range(30, 40): {'Above Average': 2600, 'Average': (1501, 2600), 'Below Average': 1500},
                range(40, 50): {'Above Average': 2500, 'Average': (1401, 2500), 'Below Average': 1400},
                range(50, 150): {'Above Average': 2400, 'Average': (1301, 2400), 'Below Average': 1300}
            },
            'Female': {
                range(20, 30): {'Above Average': 2600, 'Average': (1501, 2600), 'Below Average': 1500},
                range(30, 40): {'Above Average': 2400, 'Average': (1401, 2400), 'Below Average': 1400},
                range(40, 50): {'Above Average': 2300, 'Average': (1201, 2300), 'Below Average': 1200},
                range(50, 150): {'Above Average': 2200, 'Average': (1101, 2200), 'Below Average': 1100}
            }
        }

        for age_range, categories in age_ranges[self.gender].items():
            if self.age in age_range:
                if isinstance(categories['Average'], int):
                    if self.af2 > categories['Above Average']:
                        return 'Above Average'
                    elif self.af2 <= categories['Below Average']:
                        return 'Below Average'
                    else:
                        return 'Average'
                else:
                    min_af2, max_af2 = categories['Average']
                    if min_af2 <= self.af2 <= max_af2:
                        return 'Average'
                    elif self.af2 > max_af2:
                        return 'Above Average'
                    else:
                        return 'Below Average'

        return 'Unknown'

def calculate_af2_c(row):
    af2_calculator = AF2Calculator(row['Age'], row['Gender'], row['AF2'])
    return af2_calculator.calculate_af2_c()
class AF3Calculator(BaseVariables):
    def __init__(self, gender, af3):
        self.gender = gender
        self.af3 = af3

    def calculate_af3_c(self):
        thresholds = {
            'Male': {'Below Average': 15.3, 'Average': (15.3, 17.3), 'Above Average': 17.3},
            'Female': {'Below Average': 13.4, 'Average': (13.4, 15.6), 'Above Average': 15.6}
        }

        if self.gender in thresholds:
            gender_thresholds = thresholds[self.gender]
            if self.af3 < gender_thresholds['Below Average']:
                return 'Below Average'
            elif gender_thresholds['Below Average'] <= self.af3 <= gender_thresholds['Average'][1]:
                return 'Average'
            elif self.af3 > gender_thresholds['Above Average']:
                return 'Above Average'
            else:
                return 'Average'
        else:
            return 'Unknown'

def calculate_af3_c(row):
    af3_calculator = AF3Calculator(row['Gender'], row['AF3'])
    return af3_calculator.calculate_af3_c()

class AF4Calculator(BaseVariables):
    def __init__(self, gender, age, af4):
        self.gender = gender
        self.age = age
        self.af4 = af4

    def calculate_af4_c(self):
        thresholds = {
            'Male': {
                range(13, 20): {'Below Average': 6.01, 'Average': (6.01, 9.25), 'Above Average': 9.25},
                range(20, 30): {'Below Average': 5.61, 'Average': (5.61, 8.85), 'Above Average': 8.85},
                range(30, 40): {'Below Average': 5.21, 'Average': (5.21, 8.44), 'Above Average': 8.44},
                range(40, 50): {'Below Average': 4.81, 'Average': (4.81, 8.04), 'Above Average': 8.04},
                range(50, 150): {'Below Average': 4.00, 'Average': (4.00, 7.24), 'Above Average': 7.24},
            },
            'Female': {
                range(13, 20): {'Below Average': 4.40, 'Average': (4.40, 7.64), 'Above Average': 7.64},
                range(20, 30): {'Below Average': 4.00, 'Average': (4.00, 7.24), 'Above Average': 7.24},
                range(30, 40): {'Below Average': 3.60, 'Average': (3.60, 6.83), 'Above Average': 6.83},
                range(40, 50): {'Below Average': 3.20, 'Average': (3.20, 6.43), 'Above Average': 6.43},
                range(50, 150): {'Below Average': 2.39, 'Average': (2.39, 5.63), 'Above Average': 5.63},
            }
        }

        if self.gender in thresholds:
            gender_thresholds = thresholds[self.gender]
            for age_range, categories in gender_thresholds.items():
                if self.age in age_range:
                    if isinstance(categories['Average'], tuple):
                        min_af4, max_af4 = categories['Average']
                        if min_af4 <= self.af4 <= max_af4:
                            return 'Average'
                        elif self.af4 > max_af4:
                            return 'Above Average'
                        else:
                            return 'Below Average'
                    else:
                        if self.af4 >= categories['Above Average']:
                            return 'Above Average'
                        elif categories['Below Average'] <= self.af4 < categories['Above Average']:
                            return 'Average'
                        else:
                            return 'Below Average'
        return 'Unknown'

def calculate_af4_c(row):
    af4_calculator = AF4Calculator(row['Gender'], row['Age'], row['AF4'])
    return af4_calculator.calculate_af4_c()
class FL1Calculator(BaseVariables):
    def __init__(self, gender, age, fl1):
        self.gender = gender
        self.age = age
        self.fl1 = fl1

    def calculate_fl1_c(self):
        thresholds = {
            'Male': {
                range(20, 30): {'Below Average': 15, 'Average': (16, 24), 'Above Average': 25},
                range(30, 40): {'Below Average': 12, 'Average': (13, 21), 'Above Average': 22},
                range(40, 50): {'Below Average': 10, 'Average': (11, 17), 'Above Average': 18},
                range(50, 60): {'Below Average': 7, 'Average': (8, 15), 'Above Average': 16},
                range(60, 150): {'Below Average': 4, 'Average': (5, 13), 'Above Average': 14},
            },
            'Female': {
                range(20, 30): {'Below Average': 17, 'Average': (18, 29), 'Above Average': 30},
                range(30, 40): {'Below Average': 16, 'Average': (17, 29), 'Above Average': 30},
                range(40, 50): {'Below Average': 14, 'Average': (15, 26), 'Above Average': 27},
                range(50, 60): {'Below Average': 12, 'Average': (13, 24), 'Above Average': 25},
                range(60, 150): {'Below Average': 10, 'Average': (11, 23), 'Above Average': 24},
            }
        }

        if self.gender in thresholds:
            gender_thresholds = thresholds[self.gender]
            for age_range, categories in gender_thresholds.items():
                if self.age in age_range:
                    if isinstance(categories['Average'], tuple):
                        min_fl1, max_fl1 = categories['Average']
                        if min_fl1 <= self.fl1 <= max_fl1:
                            return 'Average'
                        elif self.fl1 >= categories['Above Average']:
                            return 'Above Average'
                        else:
                            return 'Below Average'
                    else:
                        if self.fl1 >= categories['Above Average']:
                            return 'Above Average'
                        elif categories['Below Average'] <= self.fl1 < categories['Above Average']:
                            return 'Average'
                        else:
                            return 'Below Average'
        return 'Unknown'

def calculate_fl1_c(row):
    fl1_calculator = FL1Calculator(row['Gender'], row['Age'], row['FL1'])
    return fl1_calculator.calculate_fl1_c()

class MSUB1Calculator(BaseVariables):
    def __init__(self, gender, msub1):
        self.gender = gender
        self.msub1 = msub1

    def calculate_msub1_c(self):
        thresholds = {
            'Male': {'Below Average': 5, 'Average': (5, 20), 'Above Average': 20},
            'Female': {'Below Average': 2, 'Average': (2, 14), 'Above Average': 14}
        }

        if self.gender in thresholds:
            gender_thresholds = thresholds[self.gender]
            if self.msub1 < gender_thresholds['Below Average']:
                return 'Below Average'
            elif gender_thresholds['Below Average'] <= self.msub1 <= gender_thresholds['Average'][1]:
                return 'Average'
            elif self.msub1 > gender_thresholds['Above Average']:
                return 'Above Average'
            else:
                return 'Average'
        else:
            return 'Unknown'

def calculate_msub1_c(row):
    msub1_calculator = MSUB1Calculator(row['Gender'], row['MSUB1'])
    return msub1_calculator.calculate_msub1_c()
class MSLBCalculator(BaseVariables):
    def __init__(self, gender, mslb):
        self.gender = gender
        self.mslb = mslb

    def calculate_mslb_c(self):
        thresholds = {
            'Male': {'Below Average': 27, 'Average': (28, 33), 'Above Average': 34},
            'Female': {'Below Average': 20, 'Average': (21, 28), 'Above Average': 29}
        }

        if self.gender in thresholds:
            gender_thresholds = thresholds[self.gender]
            if self.mslb >= gender_thresholds['Above Average']:
                return 'Above Average'
            elif gender_thresholds['Average'][0] <= self.mslb <= gender_thresholds['Average'][1]:
                return 'Average'
            elif self.mslb <= gender_thresholds['Below Average']:
                return 'Below Average'
            else:
                return 'Unknown'
        else:
            return 'Unknown'

def calculate_mslb_c(row):
    mslb_calculator = MSLBCalculator(row['Gender'], row['MSLB1'])
    return mslb_calculator.calculate_mslb_c()

class ME1Calculator(BaseVariables):
    def __init__(self, age, gender, me1):
        self.age = age
        self.gender = gender
        self.me1 = me1

    def calculate_me1(self):
        age_ranges = {
            'Male': {
                range(17, 20): {'Above Average': 56, 'Average': (18, 56), 'Below Average': 18},
                range(20, 30): {'Above Average': 47, 'Average': (16, 47), 'Below Average': 16},
                range(30, 40): {'Above Average': 41, 'Average': (12, 41), 'Below Average': 12},
                range(40, 50): {'Above Average': 34, 'Average': (10, 34), 'Below Average': 10},
                range(50, 60): {'Above Average': 31, 'Average': (8, 31), 'Below Average': 8},
                range(60, 150): {'Above Average': 30, 'Average': (5, 30), 'Below Average': 5}
            },
            'Female': {
                range(17, 20): {'Above Average': 30, 'Average': (6, 30), 'Below Average': 6},
                range(20, 30): {'Above Average': 32, 'Average': (8, 32), 'Below Average': 8},
                range(30, 40): {'Above Average': 28, 'Average': (6, 28), 'Below Average': 6},
                range(40, 50): {'Above Average': 20, 'Average': (4, 20), 'Below Average': 4},
                range(50, 60): {'Above Average': 16, 'Average': (3, 16), 'Below Average': 3},
                range(60, 150): {'Above Average': 12, 'Average': (2, 12), 'Below Average': 2}
            }
        }

        for age_range, categories in age_ranges[self.gender].items():
            if self.age in age_range:
                if self.me1 >= categories['Above Average']:
                    return 'Above Average'
                elif categories['Average'][0] <= self.me1 <= categories['Average'][1]:
                    return 'Average'
                elif self.me1 < categories['Below Average']:
                    return 'Below Average'

        return 'Unknown'

def calculate_me1(row):
    me1_calculator = ME1Calculator(row['Age'], row['Gender'], row['ME1'])
    return me1_calculator.calculate_me1()
class ME2Calculator(BaseVariables):
    def __init__(self, age, gender, me2):
        self.age = age
        self.gender = gender
        self.me2 = me2

    def calculate_me2(self):
        age_ranges = {
            'Male': {
                range(18, 26): {'Above Average': 49, 'Average': (31, 48), 'Below Average': 30},
                range(26, 36): {'Above Average': 45, 'Average': (29, 44), 'Below Average': 28},
                range(36, 46): {'Above Average': 41, 'Average': (23, 40), 'Below Average': 22},
                range(46, 56): {'Above Average': 35, 'Average': (18, 34), 'Below Average': 17},
                range(56, 66): {'Above Average': 31, 'Average': (13, 30), 'Below Average': 12},
                range(66, 150): {'Above Average': 28, 'Average': (11, 27), 'Below Average': 10}
            },
            'Female': {
                range(18, 26): {'Above Average': 43, 'Average': (25, 42), 'Below Average': 24},
                range(26, 36): {'Above Average': 39, 'Average': (21, 38), 'Below Average': 20},
                range(36, 46): {'Above Average': 33, 'Average': (15, 32), 'Below Average': 14},
                range(46, 56): {'Above Average': 27, 'Average': (10, 26), 'Below Average': 9},
                range(56, 66): {'Above Average': 24, 'Average': (7, 23), 'Below Average': 6},
                range(66, 150): {'Above Average': 23, 'Average': (5, 22), 'Below Average': 4}
            }
        }

        for age_range, categories in age_ranges[self.gender].items():
            if self.age in age_range:
                if self.me2 >= categories['Above Average']:
                    return 'Above Average'
                elif categories['Average'][0] <= self.me2 <= categories['Average'][1]:
                    return 'Average'
                elif self.me2 <= categories['Below Average']:
                    return 'Below Average'

        return 'Unknown'

def calculate_me2(row):
    me2_calculator = ME2Calculator(row['Age'], row['Gender'], row['ME2'])
    return me2_calculator.calculate_me2()

class ME3Calculator(BaseVariables):
    def __init__(self, me3):
        self.me3 = me3
        self.thresholds = {
            'Below Average': (None, 60),
            'Average': (60, 240),
            'Above Average': (240, None)
        }

    def calculate_me3_c(self):
        for category, (min_val, max_val) in self.thresholds.items():
            if (min_val is None or self.me3 >= min_val) and (max_val is None or self.me3 <= max_val):
                return category
        return 'Unknown'

def calculate_me3_c(row):
    me3_calculator = ME3Calculator(row['ME3'])
    return me3_calculator.calculate_me3_c()

class BL1Calculator(BaseVariables):
    def __init__(self, bl1):
        self.bl1 = bl1
        self.thresholds = {
            'Below Average': (None, 24),
            'Average': (25, 39),
            'Above Average': (40, None)
        }

    def calculate_bl1(self):
        for category, (min_val, max_val) in self.thresholds.items():
            if (min_val is None or self.bl1 >= min_val) and (max_val is None or self.bl1 <= max_val):
                return category
        return 'Unknown'

def calculate_bl1(row):
    bl1_calculator = BL1Calculator(row['BL1'])
    return bl1_calculator.calculate_bl1()

class BC1Calculator(BaseVariables):
    def __init__(self, age, gender, body_fat):
        self.age = age
        self.gender = gender
        self.body_fat = body_fat
        self.thresholds = {
            'Female': {
                (20, 40): {'Below Average': 35, 'Average': (22, 34), 'Above Average': 21},
                (40, 60): {'Below Average': 36, 'Average': (24, 35), 'Above Average': 23},
                (60, 80): {'Below Average': 37, 'Average': (25, 36), 'Above Average': 24},
            },
            'Male': {
                (20, 40): {'Below Average': 25, 'Average': (9, 24), 'Above Average': 8},
                (40, 60): {'Below Average': 27, 'Average': (12, 26), 'Above Average': 11},
                (60, 150): {'Below Average': 29, 'Average': (14, 28), 'Above Average': 13},
            }
        }

    def calculate_bc1_c(self):
        for age_range, categories in self.thresholds[self.gender].items():
            if self.age in range(*age_range):
                if isinstance(categories['Average'], int):
                    if self.body_fat >= categories['Above Average']:
                        return 'Above Average'
                    elif self.body_fat <= categories['Below Average']:
                        return 'Below Average'
                    else:
                        return 'Average'
                else:
                    min_bc1, max_bc1 = categories['Average']
                    if min_bc1 <= self.body_fat <= max_bc1:
                        return 'Average'
                    elif self.body_fat > max_bc1:
                        return 'Above Average'
                    else:
                        return 'Below Average'

        return 'Unknown'

def calculate_bc1_c(row):
    bc1_calculator = BC1Calculator(row['Age'], row['Gender'], row['BC1'])
    return bc1_calculator.calculate_bc1_c()

class MSUB2Calculator(BaseVariables):
    def __init__(self, age, gender, msub2):
        self.age = age
        self.gender = gender
        self.msub2 = msub2
        self.thresholds = {
            'Female': {
                (10, 12): {'Below Average': 11.8, 'Average': (11.8, 21.6), 'Above Average': 21.6},
                (12, 14): {'Below Average': 14.6, 'Average': (14.6, 24.4), 'Above Average': 24.4},
                (14, 16): {'Below Average': 15.5, 'Average': (15.5, 27.3), 'Above Average': 27.3},
                (16, 18): {'Below Average': 17.2, 'Average': (17.2, 29.0), 'Above Average': 29.0},
                (18, 20): {'Below Average': 19.2, 'Average': (19.2, 31.0), 'Above Average': 31.0},
                (20, 25): {'Below Average': 21.5, 'Average': (21.5, 35.3), 'Above Average': 35.3},
                (25, 30): {'Below Average': 25.6, 'Average': (25.6, 41.4), 'Above Average': 41.4},
                (30, 35): {'Below Average': 21.5, 'Average': (21.5, 35.3), 'Above Average': 35.3},
                (35, 40): {'Below Average': 20.3, 'Average': (20.3, 34.1), 'Above Average': 34.1},
                (40, 45): {'Below Average': 18.9, 'Average': (18.9, 32.7), 'Above Average': 32.7},
                (45, 50): {'Below Average': 18.6, 'Average': (18.6, 32.4), 'Above Average': 32.4},
                (50, 55): {'Below Average': 18.1, 'Average': (18.1, 31.9), 'Above Average': 31.9},
                (55, 60): {'Below Average': 17.7, 'Average': (17.7, 31.5), 'Above Average': 31.5},
                (60, 65): {'Below Average': 17.2, 'Average': (17.2, 31.0), 'Above Average': 31.0},
                (65, 150): {'Below Average': 15.4, 'Average': (15.4, 27.2), 'Above Average': 27.2},
            },
            'Male': {
                (10, 12): {'Below Average': 12.6, 'Average': (12.6, 22.4), 'Above Average': 22.4},
                (12, 14): {'Below Average': 19.4, 'Average': (19.4, 31.2), 'Above Average': 31.2},
                (14, 16): {'Below Average': 28.5, 'Average': (28.5, 44.3), 'Above Average': 44.3},
                (16, 18): {'Below Average': 32.6, 'Average': (32.6, 52.4), 'Above Average': 52.4},
                (18, 20): {'Below Average': 35.7, 'Average': (35.7, 55.5), 'Above Average': 55.5},
                (20, 25): {'Below Average': 36.8, 'Average': (36.8, 56.6), 'Above Average': 56.6},
                (25, 30): {'Below Average': 37.7, 'Average': (37.7, 57.5), 'Above Average': 57.5},
                (30, 35): {'Below Average': 36.0, 'Average': (36.0, 55.8), 'Above Average': 55.8},
                (35, 40): {'Below Average': 35.8, 'Average': (35.8, 55.6), 'Above Average': 55.6},
                (40, 45): {'Below Average': 35.5, 'Average': (35.5, 55.3), 'Above Average': 55.3},
                (45, 50): {'Below Average': 34.7, 'Average': (34.7, 54.5), 'Above Average': 54.5},
                (50, 55): {'Below Average': 32.9, 'Average': (32.9, 50.7), 'Above Average': 50.7},
                (55, 60): {'Below Average': 30.7, 'Average': (30.7, 48.5), 'Above Average': 48.5},
                (60, 150): {'Below Average': 30.2, 'Average': (30.2, 48.0), 'Above Average': 48.0}
            }
        }

    def calculate_msub2_c(self):
        age = int(self.age)
        for age_range, categories in self.thresholds[self.gender].items():
            if age >= age_range[0] and age < age_range[1]:
                if isinstance(categories['Average'], int):
                    if self.msub2 >= categories['Above Average']:
                        return 'Above Average'
                    elif self.msub2 < categories['Below Average']:
                        return 'Below Average'
                    else:
                        return 'Average'
                else:
                    min_value, max_value = categories['Average']
                    if self.msub2 >= max_value:
                        return 'Above Average'
                    elif self.msub2 < min_value:
                        return 'Below Average'
                    else:
                        return 'Average'

        return 'Unknown'

def calculate_msub2_c(row):
    msub2_calculator = MSUB2Calculator(row['Age'], row['Gender'], row['MSUB2'])
    return msub2_calculator.calculate_msub2_c()



#1 Apply the function to create the 'AF1_C' column
data['AF1_C'] = data.apply(calculate_af1_c, axis=1)
#2 Apply the function to create the 'AF2_C' column
data['AF2_C'] = data.apply(calculate_af2_c, axis=1)
#3 Apply the function to create the 'AF3' column
data['AF3_C'] = data.apply(calculate_af3_c, axis=1)
#4 Apply the function to create the 'AF4_C' column
data['AF4_C'] = data.apply(calculate_af4_c, axis=1)
#5 Apply the function to create the 'FL1_C' column
data['FL1_C'] = data.apply(calculate_fl1_c, axis=1)
#6 Apply the function to create the 'MSUB1_C' column
data['MSUB1_C'] = data.apply(calculate_msub1_c, axis=1)
#7 Apply the function to create the 'MSUB2_C' column
data['MSUB2_C'] = data.apply(calculate_msub2_c, axis=1)
#8 Apply the function to create the 'MSLB_C' column
data['MSLB_C'] = data.apply(calculate_mslb_c, axis=1)
#9 Apply the function to create the 'ME1' column
data['ME1_C'] = data.apply(calculate_me1, axis=1)
#10 Apply the function to create the 'ME2_C' column
data['ME2_C'] = data.apply(calculate_me2, axis=1)
#11 Apply the function to create the 'ME3_C' column
data['ME3_C'] = data.apply(calculate_me3_c, axis=1)
#12 Apply the function to create the 'BL1_C' column
data['BL1_C'] = data.apply(calculate_bl1, axis=1)
#13 Apply the function to create the 'BC1_C' column
data['BC1_C'] = data.apply(calculate_bc1_c, axis=1)

def count_categories(row, category):
    return row.value_counts().get(category, 0)

# Apply the count_categories function to create the AA, A, and BA columns
data['AA'] = data.apply(lambda row: count_categories(row, 'Above Average'), axis=1)
data['A'] = data.apply(lambda row: count_categories(row, 'Average'), axis=1)
data['BA'] = data.apply(lambda row: count_categories(row, 'Below Average'), axis=1)


# Print the updated data to check

print(data)

# Now you can save the updated data back to the CSV file
data.to_csv('C:/Users/Admin/Desktop/gen/GENPOP_SimData1.csv', index=False)

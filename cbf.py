import numpy as np
import random
import math

# cylinder bell funnel based on "Learning comprehensible descriptions of multivariate time series"

def generate_bell(length, amplitude, default_variance):
    bell = np.random.normal(0, default_variance, length) + amplitude * np.arange(length)/length
    return bell


def generate_funnel(length, amplitude, default_variance):
    funnel = np.random.normal(0, default_variance, length) + amplitude * np.arange(length)[::-1]/length
    return funnel


def generate_cylinder(length, amplitude, default_variance):
    cylinder = np.random.normal(0, default_variance, length) + amplitude
    return cylinder


std_generators = [generate_bell, generate_funnel, generate_cylinder]


def generate_pattern_data(length, avg_pattern_length, avg_amplitude, default_variance = 1, variance_pattern_length = 10, variance_amplitude = 2, generators = std_generators, include_negatives = True):
    data = np.random.normal(0, default_variance, length)
    current_start = random.randint(0, avg_pattern_length)
    current_length = math.ceil(random.gauss(avg_pattern_length, variance_pattern_length))
    
    while current_start + current_length < length:
        generator = random.choice(generators)
        current_amplitude = random.gauss(avg_amplitude, variance_amplitude)
        
        pattern = generator(current_length, current_amplitude, default_variance)
        
        if include_negatives and random.random() > 0.5:
            pattern = -1 * pattern
            
        data[current_start : current_start + current_length] = pattern
        
        current_start = current_start + current_length + random.randint(0, avg_pattern_length)
        current_length = max(0, math.ceil(random.gauss(avg_pattern_length, variance_pattern_length)))
    
    return data
        


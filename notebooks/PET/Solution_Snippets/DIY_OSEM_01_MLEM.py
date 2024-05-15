def MLEM(acquired_data, acq_model, initial_image, num_iterations):
    estimated_image = initial_image.clone()
    sensitivity = acq_model.backward(acquired_data.get_uniform_copy(1))
    for i in range(num_iterations):
        quotient = acquired_data/acq_model.forward(estimated_image.clone())  # y / (Ax + b)
        quotient.fill(numpy.nan_to_num(quotient.as_array()))
        mult_update = acq_model.backward(quotient.clone())/sensitivity         # A^t * quotient / A^t1
        mult_update.fill(numpy.nan_to_num(mult_update.as_array()))
    return estimated_image
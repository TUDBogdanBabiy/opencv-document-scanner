def four_point_transform(image, pts):
	# obtain a consistent order of the points
	rectangle = order_points(pts)
	(topleft, topright, bottomright, bottomleft) = rectangle
	# calculate the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((bottomright[0] - bottomleft[0]) ** 2) + ((bottomright[1] - bottomleft[1]) ** 2))
	widthB = np.sqrt(((topright[0] - topleft[0]) ** 2) + ((topright[1] - topleft[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# calculate the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((topright[0] - bottomright[0]) ** 2) + ((topright[1] - bottomright[1]) ** 2))
	heightB = np.sqrt(((topleft[0] - bottomleft[0]) ** 2) + ((topleft[1] - bottomleft[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	# now that we have the dimensions of the new image, we can create
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dest = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	# calculate the perspective transform matrix and then apply it
	Matrix = cv2.getPerspectiveTransform(rectangle, dest)
	warped = cv2.warpPerspective(image, Matrix, (maxWidth, maxHeight))
	# return the warped image
	return warped
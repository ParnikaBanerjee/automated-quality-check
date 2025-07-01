import open3d as o3d
import numpy as np

# Load both models
source = o3d.io.read_triangle_mesh("bic2.stl")
target = o3d.io.read_triangle_mesh("bicc2.stl")

# Convert to point clouds
source_pcd = source.sample_points_poisson_disk(number_of_points=100000)
target_pcd = target.sample_points_poisson_disk(number_of_points=100000)

# Pre-align with centroids (optional rough alignment)
src_center = source_pcd.get_center()
tgt_center = target_pcd.get_center()
source_pcd.translate(tgt_center - src_center)

# Run ICP
reg = o3d.pipelines.registration.registration_icp(
    source_pcd, target_pcd, 0.02, np.eye(4),
    o3d.pipelines.registration.TransformationEstimationPointToPoint()
)

print("Transformation Matrix:\n", reg.transformation)

# Apply transform and save
source_pcd.transform(reg.transformation)
o3d.io.write_point_cloud("bic_pen_aligned.ply", source_pcd)

# Visualize result
o3d.visualization.draw_geometries([source_pcd, target_pcd])

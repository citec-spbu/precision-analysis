#include <iostream>
#include "precision-analysis/Types.h"

int main() {
    Eigen::Vector3d pos(1.0, 2.0, 3.0);
    Eigen::Vector3d angles(0.1, 0.2, 0.3);
    
    PrecisionAnalysis::Point point(pos, angles);
    
    std::cout << "Position: " << point.m_position.transpose() << std::endl;
    std::cout << "Angles: " << point.m_angles.angles().transpose() << std::endl;
    
    return 0;
}
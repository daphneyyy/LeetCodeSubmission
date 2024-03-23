class ParkingSystem {
    private int big_space;
    private int medium_space;
    private int small_space;

    public ParkingSystem(int big, int medium, int small) {
        this.big_space = big;
        this.medium_space = medium;
        this.small_space = small;
    }
    
    public boolean addCar(int carType) {
        if (carType == 1) {
            if (this.big_space >= 1) {
                this.big_space -= 1;
                return true;
            }
        } else if (carType == 2) {
            if (this.medium_space >= 1) {
                this.medium_space -= 1;
                return true;
            }
        } else {
            if (this.small_space >= 1) {
                this.small_space -= 1;
                return true;
            }
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */

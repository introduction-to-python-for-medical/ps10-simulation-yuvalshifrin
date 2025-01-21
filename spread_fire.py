import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)  # גודל הרשת
    update_grid = copy.deepcopy(grid)  # יצירת עותק של הרשת

    # מעבר על כל התאים ברשת
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # אם התא מכיל עץ
                neighbors = []
                
                # בדיקה של שכנים תוך התחשבות בגבולות
                if i > 0:  # שכן עליון
                    neighbors.append(grid[i-1][j])
                if i < grid_size - 1:  # שכן תחתון
                    neighbors.append(grid[i+1][j])
                if j > 0:  # שכן שמאלי
                    neighbors.append(grid[i][j-1])
                if j < grid_size - 1:  # שכן ימני
                    neighbors.append(grid[i][j+1])
                
                # אם לפחות שכן אחד בוער, העץ הזה נשרף
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid


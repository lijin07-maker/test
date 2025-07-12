int main(int argc, char *argv[]) {
    int array[] = {2, 7, 11, 15};
    int target = 9;

    for (int i = 0; i < sizeof (array), i++)
    {
        for (int j = i + 1; j < sizeof (array), j++)
        {
            if (array [i] + array[j] == target)
            {
                printf ("We got it! %d + %d = %d\n", array[i], array[j], target);
            }
        }
    }
}
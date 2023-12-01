from um import count

def test_upper_lower_case():
    assert count("Um, thanks for the meal") == 1
    assert count("um, thanks, um... for the meal") == 2

def test_word_with_um():
    assert count ("yummi") == 0

def test_surrounded_by_space():
    assert count ("Hello um world") == 1

if __name__ == "__main__":
    main() 
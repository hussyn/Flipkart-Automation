class Locators(object):

    url = 'https://www.flipkart.com'
    number_field = '//input[@class="_2zrpKA"]'
    password_field = '//input[@type="password"]'
    submit_button = '(//span[text()="Login"])[2]'
    text_name = '//div[text()="KRISHNA KAMASKHI"]'
    '''
        Product Selecting
        '''
    cat = '//span[text()="Men"]'
    selectioncat = '//a[text()="Shirts"]'
    assertshri = '//h1[text()="Shirts"]'

    '''
    Locators for Search Text field 
    '''
    textfield = 'q'
    searchicon = "//button[@class='vh79eN']"
    textarea = "//div[contains(@class,'_3wU53n') and contains(text(), 'Nokia 6 (Matte Black, 32 GB)')]"

    '''
    Product selection
    '''

    selct = '//span[text()="Electronics"]'
    productselected = '//a[text()="Mi"]'
    subproduct = "//div[@class='_3wU53n']"
    assertofbuynow = '//span[text()="Vivo V5s Perfect Selfie (Crown Gold, 64 GB)"]'

    '''
    Button Click
    '''
    click_btm = '//button[@class="_2AkmmA _2Npkh4 _2MWPVK"]'

    '''
    CART
    '''
    cart = '//span[text()="Cart"]'
    remove_btn = '//span[text()="Remove"]'
    cart_check = "//span[text()='Check']"
    cart_size = '//a[text()="L"]'
    cart_size1 = '//a[text()="M"]'
    cart_size2 = '//a[text()="S"]'
    cart_size3 = '//a[text()="XL"]'
    cart_size4 = '//a[text()="S"]'
    cart_add_to_cart = '//button[text()="ADD TO CART"]'
    cart_elements = "//a[@class='_1TJldG _2I_hq9']"


    save_cart = '//span[text()="Save For Later"]'
    save_casrt_text = "//div[@class='_1qL_13']"

    selection_shirt = "(//a[@class='_2cLu-l'])[1]"
    wish_list = '_35Y7Yo'

    name_cou = "//div[text()='KRISHNA KAMASKHI']"
    wish_list_tag = "//div[text()='Wishlist']"
    removing_from_wishlist = '_27LgAY'
    accepting_the_pop = "//button[text()='YES, REMOVE']"
    my_profile_kri = '//div[text()="My Profile"]'
    my_pan_details = '//div[text()="PAN Card Information"]'
    text_field_name = 'pan'
    pan_name = 'fullName'
    upload_id = 'fileselect'

    '''
    Arrow

    '''

    arrow_click = 'Zhf2z-'
    add_to_cart = '//*[@id="container"]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[1]/button'
    pin_code = 'pincodeInputId'
    size_cart = '(//a[@class="_2_26Ng _5FnwXU"])[1]'
    quanity_shirt = '//div[@class="_2zH4zg"]'
    increasing_the_quanity = '//button[text()="+"]'
    amount_price = '//div[@class="_2twTWD"]/div//div/span'

    product_seventh = '//span[text()="Sports, Books & More"]'
    cricket_click = "//a[text()='Cricket']"
    # cricket_ball = "//a[@class='_2cLu-l' and text()='Sun Fly Club Cricket Leather Ball']"
    cricket_ball = "//a[contains(text(),'BAT')and @class='_2cLu-l']"

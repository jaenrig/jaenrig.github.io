#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "../src/lib.h"

/**
 * Class Lib API Test Suite
 */
class libAPI: public ::testing::Test
{
    public:
    	
        library object;

        void setUp()
        {

        }

        void TearDown()
        {

        }
};


TEST_F(libAPI, checkFunctionC)
{   
    int value = 1;
    ASSERT_EQ(object.functionC(value),1);
}
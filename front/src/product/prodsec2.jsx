import { Box, HStack, Text, VStack, GridItem } from '@chakra-ui/react'
import CustomCard from "../homepage/card";
import axios from 'axios'
import { useEffect, useState } from 'react'

import { Link, } from 'react-router-dom';
import { useParams } from 'react-router-dom';
const Prodsec2 = () => {
  const { id } = useParams();
  const [products, setProducts] = useState([]);
  const [reviews, setReviews] = useState([]);
  useEffect(() => {
    async function fetchProducts() {
      try {
        const response = await axios.get('https://ecomapi.chafaaouchaou.online/products/');
        setProducts(response.data);
      } catch (error) {
        console.error('Error fetching products:', error);
        console.error('patata patata');
      }
    }
    fetchProducts();
  }, []);
  useEffect(() => {
    const fetchReviews = async () => {
      try {
        const response = await axios.get(`https://ecomapi.chafaaouchaou.online/reviews/${id}/`);
        setReviews(response.data);
      } catch (error) {
        console.error('Error fetching reviews:', error);
      }
    };
    fetchReviews();
  }, [id]);
  return (
    <Box mt={"2rem"} display={"flex"} justifyContent={"center"}>

      <VStack margin={"0 auto"} width={"90%"} fontSize={"24px"} fontFamily={"Poppins , sans-serif"} >
        <HStack spacing={"2rem"} margin={"0 auto"}>
          <Text>
            Reviews
          </Text>
          <Text color={"#9F9F9F"}>
            Additional Information
          </Text>
          <Text color={"#9F9F9F"}>
            Reviews [5]
          </Text>
        </HStack >
        {reviews.map(review => (
          <div key={review.id}>
            <Text color={"#9F9F9F"} fontSize={"18px"} >{review.text}</Text>
          </div>
        ))}
        <HStack mt={"13rem"} display={"flex"} justifyContent={"space-around"} spacing={6} width={"100%"} mb={"2rem"} >
          {products.slice(1, 5).map(product => (
            <GridItem key={product.id} rowSpan={2} colSpan={1}>
              <Link to={`/products/${product.id}`}>
                <CustomCard
                  id={product.id}
                  imageUrl={product.photo}
                  title={product.title}
                  description={product.description}
                  price={product.price}
                />
              </Link>
            </GridItem>
          ))}
        </HStack>
      </VStack>
    </Box>
  )
}
export default Prodsec2